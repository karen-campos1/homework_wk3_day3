# Task 1: Flight Route Comparison
# Imagine you work for an airline and need to compare the flight routes of your airline with a competitor. 
# You have two sets of flight destinations, one for each airline. Write a Python program to find out:

# 1 Destinations that both airlines fly to.
# 2 Destinations unique to your airline.
# 3 Whether there are any destinations that neither airline shares.

#  Example Code:
our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

# 1 Destinations that both airlines fly to.
mutual_destinations = our_routes.intersection(competitor_routes)
print(mutual_destinations) #will print both


# 2 Destinations unique to your airline.
exclusive_flights = our_routes.difference(competitor_routes)
print(exclusive_flights)

# 3 Whether there are any destinations that neither airline shares.
unique_routes = our_routes.symmetric_difference(competitor_routes)
print(unique_routes)



# Task 1: Duplicate Entries Cleanup
# You are given a list of customer IDs, some of which are duplicated. 
# Write a Python script to remove duplicates and display the unique customer IDs.

# Example Code:

customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]
# Expected Outcome:
# A set of unique customer IDs, ensuring no duplicates. For instance, {'C001', 'C002', 'C003', 'C004'}.

no_dupes = set(customer_ids)
print(no_dupes)
customer_ids = sorted(list(no_dupes)) #extra sauce, sorted our new list (went from list to set to list again)
print(customer_ids)


