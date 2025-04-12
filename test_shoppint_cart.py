import pytest
import re
from shopping_cart import ShoppingCart




def test_can_add_item():
	my_cart = ShoppingCart(5)
	my_cart.add("Apple")
	assert my_cart.size() == 1


def test_my_item_was_added():
	my_cart = ShoppingCart(1)
	my_cart.add("Banana")
	assert "Banana" in my_cart.get_items()


def test_total_price_calculation():
	my_cart = ShoppingCart(2)
	my_cart.add("Banana")
	my_cart.add("Apple")
	assert my_cart.get_total_price == 15
	# assert my_cart.get_total_price() == 15


# @pytest.mark.xfail
# @pytest.mark.skip(reason="not implemented")
def test_cannot_exceed_max_items():
	my_cart = ShoppingCart(2)
	my_cart.add("Banana")
	my_cart.add("Apple")
	with pytest.raises(ValueError, match="Cart if full!"):
		my_cart.add("Orange")


def test_wrong_item_type():
	my_cart = ShoppingCart(1)
	with pytest.raises(ValueError, match="Item must be string"):  # TBD add assertion message to be validated
		my_cart.add(5)


def test_item_not_in_store():
	my_cart = ShoppingCart(1)
	with pytest.raises(ValueError, match=re.compile("item is missing from the inventory", re.IGNORECASE)):
	# with pytest.raises(ValueError, match="Item is missing from the inventory"):  # TBD add assertion message to be validated
		my_cart.add("koko")


# ValueError, match="Cannot place a bet with zero or negative balance."