import pytest
from src.item import Item


@pytest.fixture
def fixture_item():
    return Item("Смартфон", 10000, 20)
