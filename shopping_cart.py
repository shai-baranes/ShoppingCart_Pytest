# source: https://www.youtube.com/watch?v=YbpKMIUjvK8   (pixegami)


items_price_dict = {
	"Apple": 5,
	"Banana": 10,
	"Orange": 7,

}


# item for item in items_price_dict.values()


from typing import List

class ShoppingCart:
	"""docstring for ClassName"""
	def __init__(self, max_size: int):
		self.items = []
		self.max_size = max_size



	def add(self, item: str):
		if self.max_size == self.size():
			raise ValueError("Cart if full!")

		if not isinstance(item, str):
			raise ValueError("Item must be string")

		if item not in items_price_dict:# by default it looks at keys and not in values
		# if item not in items_price_dict.keys():# TBD to in dict
			raise ValueError("Item is missing from the inventory")

		self.items.append(item)



	def size(self):
		return len(self.items)


	def get_items(self):
		return self.items

	@property
	def get_total_price(self):
		total_price = 0
		for item in self.items:
			total_price += items_price_dict.get(item)
		return total_price






