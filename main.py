import random
from config import MODEL
from faker import Faker
fake = Faker("ru_RU")
import json


def get_title():
    with open("book.txt", "r", encoding="utf-8") as list_:
        data = list_.readlines()
        return random.choice(data)


def get_year():
    year = random.randint(1900, 2022)
    return year


def get_page():
    page = random.randint(100, 1000)
    return page


def get_isbn13():
    return fake.isbn13()


def get_rating():
    rating = random.uniform(0.0, 5.0)
    return round(rating, 2)


def get_price():
    price = random.uniform(10.5, 50.0)
    return round(price, 2)


def get_author():
    name = " ".join((fake.first_name(), fake.last_name()))
    return name


def get_field():
    return {"title": get_title(),
            "year": get_year(),
            "pages": get_page(),
            "isnb13": get_isbn13(),
            "rating": get_rating(),
            "price": get_price(),
            "author": get_author()
            }


def book_gen(inc=1):
    incr = inc
    while True:
        dict = {
            "model": MODEL,
            "pk": incr,
            "fields": get_field()}
        yield dict
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



