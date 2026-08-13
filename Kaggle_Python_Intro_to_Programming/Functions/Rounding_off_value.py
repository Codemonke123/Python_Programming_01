

import math 
# import the math module to use the ceil function
# ceiling function rounds a number up to the nearest integer

# Simple example of using the ceil function
test_value = 3.14
rounded_value = math.ceil(test_value)
print(rounded_value)

# Same example of Home Decoration for paining using ceiling function
def get_actual_cost(sqft_walls, sqft_ceiling, sqft_per_gallon, cost_per_gallon):
    total_sqft = sqft_walls + sqft_ceiling
    # gallonneed can be a decimal value, but we need to round it up to the nearest whole number since we can't buy a fraction of a gallon.
    gallonneed = total_sqft / sqft_per_gallon
    cost = cost_per_gallon * math.ceil(gallonneed)
    return cost
