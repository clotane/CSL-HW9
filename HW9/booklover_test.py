import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    def test_1_add_book(self): 
        info = BookLover("Charlie","cl@uva.edu","history")
        book1 = "Moneyball"
        rat1 = 5
        info.add_book(book1,rat1)
        self.assertTrue(any(info.book_list['book_name']==book1))

    def test_2_add_book(self):
        info2 = BookLover("Charlie","cl@uva.edu","history")
        book1 = "Moneyball"
        rat1 = 5
        info2.add_book(book1,rat1)
        info2.add_book(book1,rat1)
        bookcount = info2.book_list[info2.book_list.book_name==book1]
        self.assertTrue(len(bookcount)==1)
             
    def test_3_has_read(self): 
        info = BookLover("Charlie","cl@uva.edu","history")
        book1 = "Moneyball"
        rat1 = 5
        info.add_book(book1,rat1)
        self.assertTrue(info.has_read(book1))

    def test_4_has_read(self): 
        info = BookLover("Charlie","cl@uva.edu","history")
        book1 = "Moneyball"
        rat1 = 5
        self.assertFalse(info.has_read(book1))

    def test_5_num_books_read(self): 
        info = BookLover("Charlie","cl@uva.edu","history")
        books = [
            ('HPotter',4),
            ('Moneyball',5),
            ('Obama',4)
        ]
        for book, rating in books:
            info.add_book(book, rating)
        total = info.num_books_read()
        self.assertEqual(len(books), total)

    def test_6_fav_books(self):
        info = BookLover("Charlie","cl@uva.edu","history")
        books = [
            ('HPotter',4),
            ('Moneyball',5),
            ('Boring book',2)
        ]
        for book, rating in books:
            info.add_book(book, rating)
        favorites = info.fav_books()
        book_faves = len([rating for book, rating in books if rating >= 3])
        self.assertEqual(len(favorites),book_faves)

if __name__ == '__main__':
        
    unittest.main(verbosity=3)