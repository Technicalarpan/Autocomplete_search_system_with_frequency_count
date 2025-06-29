from trie import Trie
from collections import Counter
import heapq
from fuzzy_search import fuzzy_search
from lru_cache import LRUCache

class SearchEngine:
    def __init__(self, products_list):
        self.trie = Trie()
        self.freq_map = Counter()
        self.lru_cache = LRUCache(capacity=5)

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

        if not candidates:
             candidates = fuzzy_search(query, list(self.freq_map.keys()), max_dist=2)

        # Combine candidates with recent search history (LRU cache)
        recent = self.lru_cache.get_all()
        combined = candidates + [r for r in recent if r not in candidates]

        # Use heap to get top k by frequency, prioritizing recent searches
        def rank_key(word):
            freq = self.freq_map[word]
            recent_bonus = 1000 if word in recent else 0
            return freq + recent_bonus

        top_k = heapq.nlargest(k, combined, key=rank_key)
        return top_k

    def search_and_update(self, query):
        suggestions = self.autocomplete(query)
        if suggestions:
            selected = suggestions[0]
            self.freq_map[selected] += 1
            self.lru_cache.put(selected)
            return suggestions, selected
        else:
            return [], None
