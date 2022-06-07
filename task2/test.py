import requests

file = requests.get("https://guacamole.univ-avignon.fr/nextcloud/index.php/apps/files/?dir=/simpleText/task%202/test&openfile=928556")

print(file)


#     data.append(c._source)
# print(data.head())

# with open("data.csv", 'r') as f:
#     f.write(data.to_csv())