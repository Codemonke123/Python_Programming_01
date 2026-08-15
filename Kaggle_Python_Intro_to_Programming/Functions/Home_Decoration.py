# TODO: Finish defining the function
def get_cost(sqft_walls, sqft_ceiling, sqft_per_gallon, cost_per_gallon):
    total_sqft = sqft_walls + sqft_ceiling
    gallons_needed = total_sqft / sqft_per_gallon
    cost = cost_per_gallon * gallons_needed
    return cost

Cost_1=get_cost(1000, 500, 400, 25)
print(Cost_1)

project_cost = get_cost(432,144, 400, 15)
print(project_cost)