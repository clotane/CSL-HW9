import pandas as pd

class BookLover:
    def __init__(self, name, email, fav_genre, num_books=None, book_list=None):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = 0
        self.book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})
        
    def add_book(self, book_name, book_rating):
        new_book = pd.DataFrame({
            'book_name': [book_name],
            'book_rating': [book_rating]
        })
        if self.has_read(book_name)==False:
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
        else:
            return False
        
    def has_read(self, book_name):
        return any(self.book_list.book_name==book_name)
            
    def num_books_read(self):
        return len(self.book_list)
        
    def fav_books(self):
        return self.book_list[self.book_list.book_rating > 3]
    
    

if __name__ == '__main__':

    test_object = BookLover("charlie", "csl@virginia.edu", "nonfic")
    test_object.add_book("Moneyball", 5)
    test_object.has_read("Moneyball")
    test_object.num_books_read()
    test_object.fav_books()
    print(test_object.has_read("War of the Worlds"))
    print(test_object.num_books_read())
    print(test_object.fav_books())