import pytest
from shopping_cart import ShoppingCart, items_price_dict
from item_database import ItemDatabase


# Mock ItemDatabase for testing purposes
class MockItemDatabase:
    def __init__(self, items):
        self.items = items

    def get(self, item):
        return self.items.get(item)


# Fixture to set up a ShoppingCart instance
@pytest.fixture
def shopping_cart():
    return ShoppingCart(max_size=5)


# Fixture to set up a mock ItemDatabase
@pytest.fixture
def mock_item_database():
    return MockItemDatabase(items_price_dict)


# Test cases for ShoppingCart initialization
@pytest.mark.parametrize("max_size", [-1, 0])
def test_invalid_max_size(max_size):
    with pytest.raises(ValueError, match="Max Items value must be a positive number!"):
        ShoppingCart(max_size=max_size)


@pytest.mark.parametrize("max_size", ["five", 5.5])
def test_invalid_max_size_type(max_size):
    with pytest.raises(TypeError, match="Max Items value must be an integer!"):
        ShoppingCart(max_size=max_size)


# Test adding valid items to the cart
def test_add_item(shopping_cart):
    shopping_cart.add("Apple")
    assert shopping_cart.size() == 1
    assert "Apple" in shopping_cart.get_items()


# Test adding invalid items to the cart
@pytest.mark.parametrize("item", [123, None, True])
def test_add_invalid_item_type(shopping_cart, item):
    with pytest.raises(ValueError, match="Item must be string"):
        shopping_cart.add(item)


def test_add_item_not_in_inventory(shopping_cart):
    with pytest.raises(ValueError, match="Item is missing from the inventory"):
        shopping_cart.add("Pineapple")


# Test adding items when the cart is full
def test_add_item_to_full_cart(shopping_cart):
    for _ in range(5):  # Fill the cart to its max size
        shopping_cart.add("Apple")
    with pytest.raises(OverflowError, match="Cart if full!"):
        shopping_cart.add("Banana")


# Test calculating total price using a mocked ItemDatabase
def test_get_total_price(shopping_cart, mock_item_database):
    shopping_cart.add("Apple")
    shopping_cart.add("Banana")
    total_price = shopping_cart.get_total_price(mock_item_database)
    assert total_price == 15  # Apple (5) + Banana (10)
