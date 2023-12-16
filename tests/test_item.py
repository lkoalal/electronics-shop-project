"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
import pytest


def test__init__(fixture_item):
    assert fixture_item.name == 'Смартфон'
    assert fixture_item.price == 10000
    assert fixture_item.quantity == 20


def test_calculate_total_price(fixture_item):
    assert fixture_item.calculate_total_price() == 200000


def test_apply_discount(fixture_item):
    Item.pay_rate = 0.8
    fixture_item.apply_discount()
    assert fixture_item.price == 8000.0
