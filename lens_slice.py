toppings = ['pepperoni', 'pineapple', 'cheese', 'sausage', 'olives', 'anchovies', 'mushrooms']

prices = [2, 6, 1, 3, 2, 7, 2]

#counting $2 slices
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

#types of pizza
num_pizzas = len(toppings)

print('We sell ' + str(num_pizzas) + ' different kinds of pizza!')

#new two-dimensional toppings list
pizza_and_prices = [[3, 'canadian bacon'], [2, 'tomatoes'], [4, 'green peppers'], [3, 'onions'], [1, 'parmesan'], [2, 'chicken']]
print(pizza_and_prices)

#sorting pizza_and_prices by price from low-high
pizza_and_prices.sort()
print(pizza_and_prices)