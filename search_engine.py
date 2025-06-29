from trie import Trie
from collections import Counter
import heapq
from fuzzy_search import fuzzy_search, edit_distance
from lru_cache import LRUCache

class SearchEngine:
    def __init__(self, products_list):
        self.trie = Trie()
        self.freq_map = Counter()
        self.lru_cache = LRUCache(capacity=5)
        self.total_searches = 0
        # Insert products into trie & freq map
        for p in products_list:
            p_lower = p.lower()
            self.trie.insert(p_lower)
            self.freq_map[p_lower] = 0

    def autocomplete(self, query, k=5):
        query = query.lower()
        # 1. Try exact prefix match
        candidates = self.trie.autocomplete(query)

        if not candidates:
            # 2. Fuzzy search if no prefix matches
            candidates = fuzzy_search(query, list(self.freq_map.keys()), max_dist=2)

        recent = self.lru_cache.get_all()
        # Filter recent searches to include those relevant to the query
        recent_filtered = [r for r in recent if r in candidates or edit_distance(query, r) <= 2]

        # Combine unique candidates and recent filtered
        combined = list(set(candidates) | set(recent_filtered))

        # Ranking function prioritizes relevance first, then frequency, then recentness
        def rank_key(word):
            is_relevant = query in word
            freq = self.freq_map[word]
            recent_bonus = 1000 if word in recent_filtered else 0
            relevance_score = 1_000_000 if is_relevant else 0
            return relevance_score + freq + recent_bonus

        top_k = heapq.nlargest(k, combined, key=rank_key)
        return top_k

    def search_and_update(self, query):
        self.total_searches += 1
        suggestions = self.autocomplete(query)
        if suggestions:
            selected = suggestions[0]
            self.freq_map[selected] += 1
            self.lru_cache.put(selected)
            return suggestions, selected
        else:
            return [], None

    def show_analytics(self, top_k=5):
        print(f"\n📊 Total Searches Made: {self.total_searches}")
        print("🔝 Top searched products:")
        most_common = self.freq_map.most_common(top_k)
        for i, (product, freq) in enumerate(most_common, 1):
            bar = '█' * freq  # simple bar chart
            print(f"{i}. {product} - {freq} times {bar}")
