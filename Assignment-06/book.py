class Book:
    total_books = 0
    
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        Book.increment_book_count()
    
    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1
    
    @classmethod
    def get_total_books(cls):
        return cls.total_books
    
    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}")


if __name__ == "__main__":
    print(f"Total books before: {Book.get_total_books()}")
    
    book1 = Book("The Hobbit", "J.R.R. Tolkien", 295)
    book1.display_info()
    print(f"Total books after adding 1 book: {Book.get_total_books()}")
    
    book2 = Book("To Kill a Mockingbird", "Harper Lee", 281)
    book2.display_info()
    print(f"Total books after adding 2 books: {Book.get_total_books()}")
    
    # We can also increment manually (though typically not needed)
    Book.increment_book_count()
    print(f"Total books after manual increment: {Book.get_total_books()}")
