def cost_of_project(engraving, solid_gold):
    
   
    cost = solid_gold * (100 + 10 * len(engraving)) + (not solid_gold) * (50 + 7 * len(engraving))
    return cost

total_cost = cost_of_project("Happy Birthday", True)
print(total_cost)