import random
from config import MODEL
import json
from faker import Faker
fake = Faker("ru_RU")


def get_title() -> str:
    """
    функция для получения заголовка книги
    :return: рандомный заголовок из файла book.txt
    """
    with open("book.txt", "r", encoding="utf-8") as list_:
        data = list_.readlines()
        return random.choice(data)


def get_year() -> int:
    """
    функция для получения года
    :return: рандомный год
    """
    year = random.randint(1900, 2022)
    return year


def get_page() -> int:
    """
    функция для получения количества страниц
    :return: рандомное количество страниц
    """
    page = random.randint(100, 1000)
    return page


def get_isbn13() -> str:
    """
    функция для получения isnb
    :return: isnb из Faker
    """
    return fake.isbn13()


def get_rating() -> float:
    """
    функция для получения рейтинга
    :return: рандомный рейтинг
    """
    rating = random.uniform(0.0, 5.0)
    return round(rating, 2)


def get_price() -> float:
    """
    функция для получения цены
    :return: рандомная цена
    """
    price = random.uniform(10.5, 50.0)
    return round(price, 2)


def get_author() -> str:
    """
    функция для получения имени автора
    :return: имя из Faker
    """
    name = " ".join((fake.first_name(), fake.last_name()))
    return name


def get_field() -> dict:
    """
    функция для получения словаря с основной информацией о книге
    :return:
    """
    return {"title": get_title(),
            "year": get_year(),
            "pages": get_page(),
            "isnb13": get_isbn13(),
            "rating": get_rating(),
            "price": get_price(),
            "author": get_author()
            }


def book_gen(inc: int = 1):
    """
    Функция-генератор для получения словаря книг
    :param inc:
    :return: генератор словарей
    """
    incr = inc
    while True:
        dict_ = {
            "model": MODEL,
            "pk": incr,
            "fields": get_field()}
        yield dict_
        incr += 1


def main():
    gen = book_gen(5)
    with open("book.json", "w", encoding="utf-8") as f:
        list_ = []
        for _ in range(100):
            list_.append(next(gen))
        books_dict = json.dumps(list_, indent=4, ensure_ascii=False)
        f.write(books_dict)


if __name__ == "__main__":
    main()
