import sys

ratings_dictionary = {}

def make_dictionary(scores_file):
	
	for line in open(scores_file):
		line = line.rstrip()
		data = line.split(":")
		restaurant = data[0]
		rating = int(data[1])
		ratings_dictionary[restaurant] = rating

def sort_dictionary():
	sorted_dictionary = sorted(ratings_dictionary)
	for restaurant in sorted_dictionary:
		print "%s is rated at %d." % (restaurant, ratings_dictionary[restaurant])
	print "\n"

def random_rating():
	for restaurant, user_rating in ratings_dictionary.items():
		print restaurant
		user_rating = raw_input('What would you rate this?: ') # This doesn't assign it to the dictionary key's value
		if user_rating == "q" or user_rating == "Q":
			sort_dictionary()
			break
		else:
			ratings_dictionary[restaurant] = int(user_rating) # Assigns to the key's value


scores_file = sys.argv[1]
make_dictionary(scores_file)
sort_dictionary()

restaurant_name = raw_input('Please add a new restaurant: ')
new_restaurant_rating = int(raw_input('Now, rate it: '))

ratings_dictionary[restaurant_name] = new_restaurant_rating

sort_dictionary()

random_rating()