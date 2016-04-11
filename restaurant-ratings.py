import sys



def make_dictionary(scores_file):

	ratings_dictionary = {}
	
	for line in open(scores_file):
		line = line.rstrip()
		data = line.split(":")
		restaurant = data[0]
		rating = int(data[1])
		ratings_dictionary[restaurant] = rating

	for restaurant, rating in ratings_dictionary.items():
		print "%s is rated at %d." % (restaurant, rating)

scores_file = sys.argv[1]
make_dictionary(scores_file)