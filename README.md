# Smart Search & Autocomplete System

## Overview
This project implements a smart search system similar to e-commerce platforms like Flipkart. It supports:

- Trie-based autocomplete for fast prefix search
- Frequency-based ranking of suggestions
- Fuzzy search using Levenshtein edit distance for typo correction
- LRU cache to remember recent search queries
- Command-line interface demo for testing

## Files
- `trie.py`: Trie data structure for prefix storage and search
- `fuzzy_search.py`: Levenshtein edit distance and fuzzy search
- `lru_cache.py`: LRU cache implementation for recent queries
- `search_engine.py`: Integrates components into a search engine
- `main.py`: CLI interface to test the search system
- `products.txt`: Sample product list used to initialize the trie

## How to Run

1. Make sure you have Python 3 installed.

2. Download all files in the same folder.

3. Run the main program:
```
python main.py
```

4. Type search queries and see autocomplete suggestions.

5. Type `exit` to quit.

## How It Works

- Products are loaded into a Trie for prefix searching.
- Frequencies of product selections are tracked to rank suggestions.
- If no exact prefix matches, fuzzy search suggests products within an edit distance of 2.
- Recent searches are cached with an LRU cache and influence ranking.

## Tech Stack & Concepts
- Python 3
- Data Structures: Trie, Heap, Doubly Linked List (for LRU Cache)
- Algorithms: Levenshtein Edit Distance, Heap-based Top-K selection
- Concepts: Autocomplete, Search Ranking, Caching

## License
MIT License
Created an autocomplete search engine that predicts product names from user input. It monitors search frequency for every term and orders suggestions so that the most searched ones are listed first. It also supports fuzzy search based on Levenshtein edit distance to support typos and offer relevant suggestions even with errors in the query. This optimizes user experience by offering quick, accurate, and intelligent search results.