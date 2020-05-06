###### Boredless Tourist App ######

###### List ######

# destinations
destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "Sao Paulo, Brazil", "Cairo, Egypt"]

# test data for traveler
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]


###### Functions ######

# gets dest index
def get_destination_index(destination):
  try:
    destination_index = destinations.index(destination)
    return destination_index
  except ValueError:
    return destination + " is not in the list."

# gets traveler location:
def get_traveler_location(traveler):
  traveler_destination = traveler[1]
  traveler_destination_index = get_destination_index(traveler_destination)
  return traveler_destination_index

# adds attraction
def add_attraction(destination, attraction):
  try:
    destination_index = get_destination_index(destination)
    attractions_for_destination = attractions[destination_index].append(attraction)
  except ValueError:
    return

# finds attractions
def find_attractions(destination, interests):

    destination_index = get_destination_index(destination)
    attractions_in_city = attractions[destination_index]
    attractions_with_interest = []

    for attraction in attractions_in_city:
        possible_attraction = attraction
        attraction_tags = attraction[1] # retrieves tagged info on attraction

        for interest in interests:
            if interest in attraction_tags:
                attractions_with_interest.append(possible_attraction[0])

        return attractions_with_interest





###### Body ######

# body of code
test_destination_index = get_traveler_location(test_traveler)

attractions = [[] for destination in destinations]

###### Attractions ######


add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("Los Angeles, USA", ['Venice Beach', ['beach']])
add_attraction("Sao Paulo, Brazil", ["Sao Paulo Zoo", ["zoo"]])
add_attraction("Sao Paulo, Brazil", ["Patio do Colegio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

###### test print functions ######

# print(get_destination_index("Los Angeles, USA"))
# print(get_destination_index("Paris, France"))
# print(get_destination_index("Hyderabad, India"))
# print(test_destination_index)

# print(attractions)
la_arts = find_attractions("Los Angeles, USA", ['art'])
china_garden = find_attractions("Shanghai, China", ['garden'])
print(la_arts)
print(china_garden)
