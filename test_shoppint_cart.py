import pytest
import re
from shopping_cart import ShoppingCart
from item_database import ItemDatabase
from unittest.mock import Mock

# TBD later add parametrized fixtures


@pytest.fixture
def single_item_cart():
	return ShoppingCart(1)

@pytest.fixture
def dual_items_cart():
	return ShoppingCart(2)




def test_can_add_item():
	my_cart = ShoppingCart(5)
	my_cart.add("Apple")
	assert my_cart.size() == 1
 

def test_my_item_was_added(single_item_cart):
	# my_cart = ShoppingCart(1)
	single_item_cart.add("Banana")
	assert "Banana" in single_item_cart.get_items()


def test_total_price_calculation_1(dual_items_cart):
	# my_cart = ShoppingCart(2)
	dual_items_cart.add("Banana")
	dual_items_cart.add("Apple")
	item_database = ItemDatabase()
	item_database.get = Mock(return_value=1.0) # assuming the get is not implemented yet hence using Mock
	assert dual_items_cart.get_total_price(item_database) == 2


def test_total_price_calculation_2(dual_items_cart):
	# my_cart = ShoppingCart(2)
	dual_items_cart.add("Banana")
	dual_items_cart.add("Apple")

	item_database = ItemDatabase()

	def mock_get_item(item):
		if item == "Banana":
			return 1
		if item == "Apple":
			return 2


	item_database.get = Mock(side_effect=mock_get_item) # since we want to mock different prices to diff items (try lambda)

	assert dual_items_cart.get_total_price(item_database) == 3
	# assert my_cart.get_total_price() == 15


# @pytest.mark.xfail
# @pytest.mark.skip(reason="not implemented")
def test_cannot_exceed_max_items(dual_items_cart):
	# my_cart = ShoppingCart(2)
	dual_items_cart.add("Banana")
	dual_items_cart.add("Apple")
	with pytest.raises(OverflowError, match="Cart if full!"):
		dual_items_cart.add("Orange")


def test_wrong_item_type(single_item_cart):
	# my_cart = ShoppingCart(1)
	with pytest.raises(ValueError, match="Item must be string"):  # TBD add assertion message to be validated
		single_item_cart.add(5)


def test_item_not_in_store(single_item_cart):
	# my_cart = ShoppingCart(1)
	with pytest.raises(ValueError, match=re.compile("item is missing from the inventory", re.IGNORECASE)):
	# with pytest.raises(ValueError, match="Item is missing from the inventory"):  # TBD add assertion message to be validated
		single_item_cart.add("koko")

# @pytest.mark.skip(reason="not implemented")
def test_class_instantite_with_non_positive_value():
	with pytest.raises(ValueError, match=re.compile("max Items value must be a positive number!", re.IGNORECASE)):
		my_cart = ShoppingCart(0)
	with pytest.raises(ValueError, match=re.compile("max Items value must be a positive number!", re.IGNORECASE)):
		my_cart = ShoppingCart(-1)


# @pytest.mark.skip(reason="not implemented")
def test_class_instantite_with_non_integer_value():
	with pytest.raises(TypeError):
		my_cart = ShoppingCart("a")
	with pytest.raises(TypeError, match=re.compile("max Items value must be an integer!", re.IGNORECASE)):
		my_cart = ShoppingCart(5.3)


