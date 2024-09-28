class HashTable:
    def __init__(self, size):
        """Initialize the hash table with a given size."""
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        """Hash function to determine the index for a given key."""
        # Calculate the ASCII sum of the key
        ascii_sum = sum(ord(char) for char in key)
        # Determine index using the hash function
        return ascii_sum % self.size

    def insert(self, key):
        """Insert a key with its ASCII sum as the value into the hash table."""
        index = self.hash_function(key)
        ascii_sum = sum(ord(char) for char in key)
        
        # Check if the index is already filled
        if self.table[index] is not None:
            print(f"Error: Index {index} already filled with key '{self.table[index][0]}' and value '{self.table[index][1]}'.")
        else:
            # Insert the key and its ASCII sum as the value
            self.table[index] = (key, ascii_sum)
            print(f"Inserted key '{key}' (ASCII Sum: {ascii_sum}) at index {index}.")

    def delete(self, key):
        """Delete the value associated with the given key."""
        index = self.hash_function(key)
        if self.table[index] and self.table[index][0] == key:
            self.table[index] = None
            print(f"Deleted key '{key}' from index {index}.")
        else:
            print(f"Key '{key}' not found at index {index}.")

    def search(self, key):
        """Search for the value associated with the given key."""
        index = self.hash_function(key)
        if self.table[index] and self.table[index][0] == key:
            print(f"Found key '{key}' with value '{self.table[index][1]}' at index {index}.")
            return self.table[index][1]
        print(f"Key '{key}' not found.")
        return None

    def traverse(self):
        """Traverse and print all key-value pairs in the hash table."""
        print("\nHash Table Contents:")
        for index, item in enumerate(self.table):
            if item is not None:
                key, value = item
                print(f"Index {index}: Key '{key}', Value '{value}'")
            else:
                print(f"Index {index}: Empty")

def display_menu():
    """Display the CLI menu options."""
    print("\nHash Table Operations:")
    print("1. Insert a key")
    print("2. Delete a key")
    print("3. Search for a key")
    print("4. Traverse the hash table")
    print("5. Exit")

if __name__ == "__main__":
    # Create a hash table with a fixed size
    size = int(input("Enter the size of the hash table: "))
    hash_table = HashTable(size)

    while True:
        display_menu()
        choice = input("\nEnter your choice (1-5): ")

        if choice == '1':
            key = input("Enter the key (string): ")
            hash_table.insert(key)

        elif choice == '2':
            key = input("Enter the key to delete: ")
            hash_table.delete(key)

        elif choice == '3':
            key = input("Enter the key to search: ")
            hash_table.search(key)

        elif choice == '4':
            hash_table.traverse()

        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
