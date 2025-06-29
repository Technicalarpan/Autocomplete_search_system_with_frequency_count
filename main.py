import speech_recognition as sr
from search_engine import SearchEngine

def get_voice_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙️ Speak your search query...")
        audio = r.listen(source, timeout=5)
    try:
        text = r.recognize_google(audio)
        print(f"🗣️ You said: {text}")
        return text
    except sr.UnknownValueError:
        print("❌ Sorry, could not understand your speech.")
        return ""
    except sr.RequestError as e:
        print(f"❌ Error with Google Speech API: {e}")
        return ""

def load_products(filename):
    with open(filename, "r") as f:
        products = [line.strip() for line in f.readlines() if line.strip()]
    return products

def main():
    print("Loading product list...")
    products = load_products("products.txt")
    engine = SearchEngine(products)
    print("Smart Search & Autocomplete System Initialized.")

    while True:
        query = input("Type your search query or 'voice' to speak, 'analytics' for stats, 'exit' to quit:\nSearch: ").strip()

        if query.lower() == 'exit':
            print("Exiting...")
            break

        elif query.lower() == 'analytics':
            engine.show_analytics()
            continue

        elif query.lower() == 'voice':
            query = get_voice_input().strip()
            if not query:
                print("No voice input detected.")
                continue

            # Immediately process voice query
            suggestions, selected = engine.search_and_update(query)
            if suggestions:
                print(f"Suggestions: {suggestions}")
                print(f"Selected: {selected}")
            else:
                print("No suggestions found.")
            continue

        # Normal typed query processing
        suggestions, selected = engine.search_and_update(query)
        if suggestions:
            print(f"Suggestions: {suggestions}")
            print(f"Selected: {selected}")
        else:
            print("No suggestions found.")

if __name__ == "__main__":
    main()
