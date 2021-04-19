class Pizza:

    def __init__(self):
        self.toppings = []

    def add_topping(self, topping):
        self.toppings.append(topping.lower())
        return self

    def display_toppings(self):
        print("This Pizza has:")
        for topping in self.toppings:
            print(topping.capitalize())


'''            
    #Please take a closer look at this method:
    def add_topping(self, topping):
        self.toppings.append(topping.lower())
        return self

    The last line is what allows method chaining. It returns self (the instance that called the method), so you can use it to call another method in the same line.

'''
pizza = Pizza()

pizza.add_topping("mushrooms").add_topping("olives").add_topping("chicken").display_toppings()

print()
pizza.add_topping("salad") \
    .add_topping("tomatoes") \
    .add_topping("onion") \
    .display_toppings()

pizza.display_toppings()

# pizza.add_topping("mushrooms") IS self, en self is pizza! dus nadat pizza.add_topping("mushrooms") is uitgevoerd staat er eigenlijk
# pizza.add_topping("olives").add_topping("chicken").display_toppings()