def show_menu():
    print("=" * 30)
    print("Book Management System (CLI Version)")
    print("1. Add a Book")
    print("2. Query a Book (by ISBN)")
    print("3. Exit the Program")
    print("=" * 30)

def add_book():
    isbn = input("Enter the book's ISBN: ")
    title = input("Enter the book's title: ")
    author = input("Enter the book's author: ")
    with open("data.txt", "a", encoding="utf-8") as file:
        file.write(f"{isbn},{title},{author}\n")
    print(f"✅ Book '{title}' added successfully!")

def query_book():
    target_isbn = input("Enter the ISBN to query: ")
    found = False
    with open("data.txt", "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            isbn, title, author = line.split(",")
            if isbn == target_isbn:
                print(f"\n📚 Book found:")
                print(f"ISBN: {isbn}")
                print(f"Title: {title}")
                print(f"Author: {author}")
                found = True
                break
    if not found:
        print(f"❌ No book found with ISBN {target_isbn}")

if __name__ == "__main__":
    print("Welcome to the Book Management System!")
    while True:
        show_menu()
        choice = input("Enter your choice (1-3): ")
        if choice == "1":
            add_book()
        elif choice == "2":
            query_book()
        elif choice == "3":
            print("👋 Thank you for using the system. Goodbye!")
            break
        else:
            print("⚠️ Invalid input. Please enter a number between 1 and 3.")