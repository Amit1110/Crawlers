import json

with open('imdb.json') as json_data:
    d = json.load(json_data)

counter=1
for data in d:
	print(str(counter)+"\n")
	print("Name of the movie: " + data['name'])
	print("Collections of this week: " + data['colthis'])
	print("Gross Collections: " + data['colwhole'])
	print("Number of weeks passed: " + data['weeks'])
	counter+=1
	print("\n")
