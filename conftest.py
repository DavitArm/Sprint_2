from main import BooksCollector
import pytest


@pytest.fixture(scope='function')
def collector():
    book_collector = BooksCollector()
    return book_collector
