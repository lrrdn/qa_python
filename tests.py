from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_new_book_add_existing_book_not_added(self):
        collector = BooksCollector()
        collector.add_new_book('Война и мир')
        collector.add_new_book('Война и мир')

        assert len(collector.get_books_rating()) == 1

    def test_set_book_rating_not_existing_book_not_added(self):
        collector = BooksCollector()
        collector.add_new_book('Портрет Дориана Грея')
        collector.set_book_rating('Война и мир', 5)

        assert 'Война и мир' not in collector.get_books_rating().keys()

    def test_set_book_rating_more_than_10_not_added(self):
        collector = BooksCollector()
        collector.add_new_book('Мы')
        collector.set_book_rating('Мы', 15)

        assert collector.get_book_rating('Мы') == 1

    def test_set_book_rating_less_than_1_not_added(self):
        collector = BooksCollector()
        collector.add_new_book('Идиот')
        collector.set_book_rating('Идиот', 0.5)

        assert collector.get_book_rating('Идиот') == 1

    def test_set_book_rating_correct_value(self):
        collector = BooksCollector()
        collector.add_new_book('Доктор Живаго')
        collector.set_book_rating('Доктор Живаго', 7)

        assert collector.get_book_rating('Доктор Живаго') == 7

    def test_get_book_rating_existing_book_correct_value(self):
        collector = BooksCollector()
        collector.add_new_book('Над пропастью во ржи')

        assert collector.get_book_rating('Над пропастью во ржи') == 1

    def test_get_book_rating_not_existing_book(self):
        collector = BooksCollector()
        collector.add_new_book('Мастер и Маргарита')

        assert collector.get_book_rating('Маленький принц') is None

    def test_get_books_with_specific_rating_correct_rating_existing_books(self):
        collector = BooksCollector()
        collector.add_new_book('Маленький принц')
        collector.add_new_book('Горе от ума')
        collector.add_new_book('Финансист')
        collector.add_new_book('Собор Парижской Богоматери')
        collector.set_book_rating('Финансист', 8)
        collector.set_book_rating('Горе от ума', 8)

        assert len(collector.get_books_with_specific_rating(8)) == 2

    def test_get_books_rating_not_empty_collection(self):
        collector = BooksCollector()
        collector.add_new_book('Маленький принц')
        collector.add_new_book('Горе от ума')
        collector.add_new_book('Финансист')
        collector.add_new_book('Собор Парижской Богоматери')

        assert len(collector.get_books_rating()) == 4

    def test_add_book_in_favorites_existing_book_added(self):
        collector = BooksCollector()
        collector.add_new_book('Великий Гэтсби')
        collector.add_book_in_favorites('Великий Гэтсби')

        assert len(collector.get_list_of_favorites_books()) == 1

    def test_add_book_in_favorites_not_existing_book_not_added(self):
        collector = BooksCollector()
        collector.add_new_book('Мартин Иден')
        collector.add_book_in_favorites('Лолита')

        assert len(collector.get_list_of_favorites_books()) == 0

    def test_delete_book_from_favorites_existing_in_favorites_book(self):
        collector = BooksCollector()
        collector.add_new_book('Анна Каренина')
        collector.add_book_in_favorites('Анна Каренина')
        collector.delete_book_from_favorites('Анна Каренина')

        assert len(collector.get_list_of_favorites_books()) == 0

    def test_delete_book_from_favorites_not_existing_in_favorites_book(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.delete_book_from_favorites('1984')

        assert len(collector.get_list_of_favorites_books()) == 0

    def test_get_list_of_favorites_books_empty_list(self):
        collector = BooksCollector()
        collector.add_new_book('Человек-Невидимка')

        assert len(collector.get_list_of_favorites_books()) == 0

    def test_get_list_of_favorites_books_not_empty_list(self):
        collector = BooksCollector()
        collector.add_new_book('Грозовой перевал')
        collector.add_new_book('Братья Карамазовы')
        collector.add_new_book('Убить пересмешника')
        collector.add_book_in_favorites('Грозовой перевал')
        collector.add_book_in_favorites('Убить пересмешника')

        assert len(collector.get_list_of_favorites_books()) == 2
