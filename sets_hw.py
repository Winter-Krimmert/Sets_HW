





# Task 1 Flight Route Comparison
# 1. mutual destinations
our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}
mutual_destinations = our_routes.intersection(competitor_routes)
print(mutual_destinations)

# 2. destinations unique to your airline

# Difference
# what is in set1 that is not in set2 
# order of sets matters
our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}
unique_our_routes = (our_routes).difference(competitor_routes)
print(unique_our_routes)

# 3 Are their elements that neither set shares?
# Whether there are any destinations that neither airline shares.

if our_routes.isdisjoint(competitor_routes):
    print("The sets don't share any common elements. ")
else:
    print("The sets have common elements. ")


# Set Operations in Data Analysis
# Task 1 Duplicate Entries Cleanup

customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]

customer_ids = set(customer_ids)
print(customer_ids)