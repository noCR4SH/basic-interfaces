class Bookshelf:
    def __init__(self):
        self.books = ["Book 1", "Book 2", "Book 3"]
    
    def __getitem__(self, index):
        return self.books[index]
    
    def __setitem__(self, index, value):
        self.books[index] = value

    # def __iter__(self):
    #     return iter(self.books)
    

    

shelf = Bookshelf()
print("Old book: " + shelf[1])

shelf[1] = "Super cool new book!"

print("New book: " + shelf[1])

print("\nAll books:")
for book in shelf:
    print(book)