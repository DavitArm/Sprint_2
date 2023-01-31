class TestBooksCollector:


    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_rating()) == 2

    def test_add_new_book_cant_if_add_same_book(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert len(collector.get_books_rating()) == 1

    def test_set_book_rating_cant_if_the_book_is_not_listed(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        book_not_listed = 'Что делать, если ваш кот хочет вас убить'
        collector.set_book_rating(book_not_listed, 2)
        assert collector.get_book_rating(book_not_listed) is None

    def test_set_book_rating_cant_if_rate_less_than_one(self, collector):
        book = 'Гордость и предубеждение и зомби'
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_rating(book, -1)
        assert collector.get_book_rating(book) == 1

    def test_set_book_rating_cant_if_rate_more_than_ten(self, collector):
        book = 'Гордость и предубеждение и зомби'
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_rating(book, 11)
        assert collector.get_book_rating(book) == 1

    def test_get_book_rating_book_not_added_has_no_rating(self, collector):
        book = 'Гордость и предубеждение и зомби'
        assert collector.get_book_rating(book) is None

    def test_add_book_in_favorites(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert collector.get_list_of_favorites_books() == ['Гордость и предубеждение и зомби']

    def test_add_book_in_favorites_cant_if_book_not_in_dictionary(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_list_of_favorites_books()) == 0

    def test_delete_book_from_favorites(self, collector):
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')
        assert len(collector.get_list_of_favorites_books()) == 0
