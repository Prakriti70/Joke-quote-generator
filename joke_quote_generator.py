import random

def load_file(filename):
    """Load lines from a file and return as a list, removing empty lines."""
    with open(filename, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip()]

def main():
    jokes = load_file("jokes.txt")
    quotes = load_file("quotes.txt")

    choice = input("Type 'joke' for a random joke or 'quote' for a random quote: ").lower()

    if choice == "joke":
        print("\nHere's a joke for you:")
        print(random.choice(jokes))
    elif choice == "quote":
        print("\nHere's a quote for you:")
        print(random.choice(quotes))
    else:
        print("Invalid choice! Please type 'joke' or 'quote'.")

if __name__ == "__main__":
    main()
