# Create a Python function that takes a list of tuples as an argument.
# Each tuple contains information about a flight itinerary: 
# (traveler_name, origin, destination). 
# The function should format and return a string that lists each itinerary. 
# For example, if the input is [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")], the output should be a string formatted as:

# "Itinerary 1: Alice - From New York to London
#  Itinerary 2: Bob - From Tokyo to San Francisco"

itineraries = [("Sarah", "Denver", "Orlando"), ("Michael", "San Francisco", "Boston"), ("Olivia", "Little Rock", "Scottsdale")]
#    function name      #parameter of my tuple
def format_itineraries(itineraries):
    # empty string to add my tuple info to for later
    formatted = ""
#    index     list        count     parameter     instead of start @ 0, start @1
    for index, itinerary in enumerate(itineraries, start=1):
# set variable names: unpacking the tuple                           
        traveler_name, origin, destination = itinerary
 #formatted += . concatenates the formatted string for the current itinerary to the existing content stored in the formatted variable
        formatted += f"Itinerary {index}: {traveler_name} - From {origin} to {destination}\n"
    return formatted

print(format_itineraries(itineraries)) 




# Task 1: Library System Enhancement
# Sharpen your skills in managing and modifying data within tuples and lists.

# Problem Statement:
# You are maintaining a library system where each book is stored as a tuple within a list. Your task is to update this system by adding new books and ensuring no duplicates.
# Add functionality to insert new books into library.
# Ensure that adding a duplicate book is handled appropriately.
# Existing Library Data:

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

def add_books(book):
    for title, author in library:
        if book[1] == title:
            print("That book is already in your library.")
            return library
    library.append(book)
    return library

print(add_books(("The Hobbit", "J.R.R. Tolkien")))
print(add_books(("Twilight", "Stephanie Meyer")))





# Problem Statement: 
# You are given a list of tuples, each representing a customer's order. 
# Each tuple contains the customer's name, the product ordered, and the quantity. 
# Your task is to unpack each tuple and print the order details in a user-friendly format.

# Sample Order Data:


orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    ("Ashley", "Phone Charger", 3),
    ("Fred", "Desktop Computer", 1)
]

for client, order, quantity in orders:
    print(f"{client}'s order: {order} x {quantity}")