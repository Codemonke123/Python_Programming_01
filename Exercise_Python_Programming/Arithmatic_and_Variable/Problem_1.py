# Create variables
num_years = 4
days_per_year = 365 
hours_per_day = 24
mins_per_hour = 60
secs_per_min = 60

# Calculate number of seconds in four years
total_secs = secs_per_min * mins_per_hour * hours_per_day * days_per_year * num_years
print(total_secs)

#In general, to work with a variable, you need to begin by selecting the name you want to use. Variable names are ideally short and descriptive. They also need to satisfy several requirements:

# 1.They can't have spaces (e.g., test var is not allowed)
# 2.They can only include letters, numbers, and underscores (e.g., test_var! is not allowed)
# 3.They have to start with a letter or underscore (e.g., 1_var is not allowed)