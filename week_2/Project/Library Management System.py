class Book:
    def __init__(self,title,author,publish_year) -> None:
        self.title=title
        self.author=author
        self.publish_year=publish_year
        self.is_avaiable=True

class Library:
    def __init__(self,name) -> None:
        self.name=name
        self.books=[]

    def add_book(self,book):
        self.books.append(book)
        print(f'Book {book.title} added to the library')

    def remove_book(self,book):
        if book in self.books:
            self.books.remove(book)
            print(f'Book {book.title} remove successfully from the library')
        else:
            print('Book is not available in the library')


    def search_by_title(self,title):
        for book in self.books:
            if book.title==title:
                print(f'Book {book.title} is available in the library')
                return
        print(f'No book in title {book.title} is available in the library')


    def search_by_author(self,author):
        found_books=[]
        for book in self.books:
            if book.author==author:
                found_books.append(book)
        if found_books:
            print(f'Books by author {book.author}')
            for book in found_books:
                print(f'-- {book.title}')
        else:
            print(f'NO book found by author {author} in the library')
    

    def display_all_books(self):
        print('All books is here')
        for book in self.books:
            availability='Available' if book.is_avaiable else 'Not available'
            print(f'Author name:{book.author}, Title name:{book.title}, Published year:{book.publish_year}')

    
# create book object
book1=Book('c++','tamim',2013)
book2=Book('java','karim',2013)
book3=Book('python','rahim',2043)

# create library object
library=Library('my library')

#add book to the library
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Display all book to the library
library.display_all_books()

# search book by a title
library.search_by_title('java')
library.search_by_title('2043')

#search book by author 
library.search_by_author('rahim')
library.search_by_author('java')

# Remove a book from the library
library.remove_book(book3)

# Display all book after remove the library
library.display_all_books()