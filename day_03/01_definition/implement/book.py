class Book:
    def __init__(self, title=None, genre=None, author=None):
        self.title = title
        self.genre = genre
        self.author = author
    
    def __repr__(self):
        return f"{self.title}, {self.genre} by {self.author}"
        
book = Book("The Hobbit", "Fantasy", "Tolkien")
print(book)