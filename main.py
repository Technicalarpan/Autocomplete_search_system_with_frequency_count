from search_engine import SearchEngine

def load_products(filename):
    with open(filename, "r") as f:
        products = [line.strip() for line in f.readlines() if line.strip()]
    return products

def main():
    print("Loading product list...")
    products = load_products("products.txt")
    engine = SearchEngine(products)
    print("Smart Search & Autocomplete System Initialized.")

    print("Type your search query and press Enter. Type 'exit' to quit.")
    while True:
        query = input("Search: ").strip()
        if query.lower() == "exit":
            print("Exiting...")
            break
        suggestions, selected = engine.search_and_update(query)
        if suggestions:
            print(f"Suggestions: {suggestions}")
            print(f"Selected: {selected}")
        else:
            print("No suggestions found.")

if __name__ == "__main__":
    main()
