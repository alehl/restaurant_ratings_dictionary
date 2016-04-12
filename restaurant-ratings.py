import sys

ratings_dictionary = {}

def make_dictionary(scores_file):
	
	for line in open(scores_file):
		line = line.rstrip()
		data = line.split(":")
		restaurant = data[0]
		rating = int(data[1])
		ratings_dictionary[restaurant] = rating

# def print_dictionary():
# 	for restaurant, rating in sorted_dictionary.items():
# 		print "%s is rated at %d." % (restaurant, rating)
# 	print "\n"

def sort_dictionary():
	sorted_dictionary = sorted(ratings_dictionary)
	for restaurant in sorted_dictionary:
		print "%s is rated at %d." % (restaurant, ratings_dictionary[restaurant])
	print "\n"

scores_file = sys.argv[1]
make_dictionary(scores_file)
sort_dictionary()

restaurant_name = raw_input('Please add a new restaurant: ')
new_restaurant_rating = int(raw_input('Now, rate it: '))

ratings_dictionary[restaurant_name] = new_restaurant_rating

sort_dictionary()


