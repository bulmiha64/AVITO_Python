import json
import keyword
import pytest


class Advert:
    def __init__(self, json: dict):
        for key, value in json.items():
            if keyword.iskeyword(key):
                self.__dict__[key + '_'] = value
            elif (isinstance(value, dict)):
                self.__dict__[key] = Advert(value)
            else:
                if key == "price" and value < 0:
                    raise ValueError
                self.__dict__[key] = value

    def __getattr__(self, item):
        if item == 'price':
            return 0
        else:
            raise AttributeError

    def __setattr__(self, key, value):
        if key == 'price' and value < 0:
            raise ValueError
        else:
            super().__setattr__(key, value)

    def __repr__(self):
        return f'{self.title} | {self.price} ₽'


def test_advert_dict_empty():
    lesson_str = """{}"""
    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)
    assert not (bool(lesson_ad.__dict__) and all(lesson_ad.__dict__.values()))


def test_advert():
    lesson_str = """{
        "title": "python",
        "class" : "2",
        "location": {
            "address": "город Москва, Лесная, 7",
            "metro_stations": ["Белорусская"]
            }
        }"""
    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)
    lesson_ad.title
    lesson_ad.class_
    lesson_ad.location.address
    lesson_ad.location.metro_stations


def test_advert_price_none():
    lesson_str = """{
            "title": "python",
            "class" : "2",
            "location": {
                "address": "город Москва, Лесная, 7",
                "metro_stations": ["Белорусская"]
                }
            }"""
    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)
    assert lesson_ad.price == 0


def test_advert_price():
    lesson_str = """{
            "title": "python",
            "price": 195,
            "class" : "2",
            "location": {
                "address": "город Москва, Лесная, 7",
                "metro_stations": ["Белорусская"]
                }
            }"""
    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)
    assert lesson_ad.price == 195


def test_advert_price_negative():
    lesson_str = """{
            "title": "python",
            "price": -291,
            "class" : "2",
            "location": {
                "address": "город Москва, Лесная, 7",
                "metro_stations": ["Белорусская"]
                }
            }"""
    lesson = json.loads(lesson_str)
    with pytest.raises(ValueError):
        Advert(lesson)


def test_advert_settlement():
    lesson_str = """{
                "title": "python",
                "price": 195,
                "class" : "2",
                "location": {
                    "address": "город Москва, Лесная, 7",
                    "metro_stations": ["Белорусская"]
                    }
                }"""
    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)
    print(vars(lesson_ad))
    assert lesson_ad.location.settlement == "город Москва"
