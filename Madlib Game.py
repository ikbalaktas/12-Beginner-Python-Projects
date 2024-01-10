#In this project I created a Madlib game which you need to give an adjective, two verbs and a famous name to fill in the blanks.

adjective = input("An adjective: ")
verb1 = input("A verb: ")
verb2 = input("Another verb: ")
famous_name = input("Name of a famous: ")

print(f"Computer programming is so {adjective}! It makes me  so excited all the time because I love to {verb1}. \
Stay hydrated and {verb2} like {famous_name}.")

#There are also two more ways to print a line including variables in it.

#print("Computer programming is so {}! It makes me  so excited all the time because I love to {}. \
#Stay hydrated and {} like {}.".format(adjective, verb1, verb2, famous_name))

#print("Computer programming is so {0}! It makes me  so excited all the time because I love to {2}. \
#Stay hydrated and {1} like {3}.".format(adjective, verb1, verb2, famous_name))
#The example above changes the order of verbs by using index numbers. 