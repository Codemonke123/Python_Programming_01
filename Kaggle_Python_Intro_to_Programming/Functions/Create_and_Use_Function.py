# TODO: Complete the function
# Basic use of function for repetitive tasks
def get_expected_cost(beds, baths):
    Hcost = 80000
    bedrooms = 30000
    bathrooms = 10000
    value = Hcost + bedrooms * beds + bathrooms * baths
    return value

option_one = get_expected_cost(2,3)
option_two = get_expected_cost(3,2)
option_three = get_expected_cost(3,3)
option_four = get_expected_cost(3,4)
print(option_one)
print(option_two)
print(option_three)
print(option_four)