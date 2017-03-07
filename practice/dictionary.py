weekend = {"sun": "sunday","Mon": "Monday"}
capitals = {}
capitals["svk"] = "Bratislava"
capitals["deu"] = "Berlin"
capitals["dnk"] = "Copenhagen"

# print weekend["sun"]
# print capitals["svk"]
#
# for data in capitals:
#     print data
# for key in capitals.iterkeys():
#     print key
# for val in capitals.itervalues():
#     print val
# for key.data in capitals.iteritems():
#     print key, "=", data

# print  cmp(weekend,capitals)
#
# print len(weekend)
# print str(capitals)
# print type(weekend)
# dict2 =  capitals.copy()
# print dict2
# print capitals.items()

# context = {
#     'questions': [
#         {'id': 1, 'content': 'Why is there a light in the fridge and not in the freezer?'},
#         {'id': 2, 'content': 'Why don\'t sheep shrink when it rains?'},
#         {'id': 3, 'content': 'Why are they called apartments when they are all stuck together'},
#         {'id': 4, 'content': 'Why do cars drive on the parkway and park on the driveway'}
#     ]
# }
#
# for key, data in context.items():
#     for value in data:
#         print "Question #", value["id"], ":", value["content"]
#         print "---"

# data = {"house":"Haus","cat":"Katze","red":"rot"}
# print data.items()
# print data.keys()
# print data.values()

dishes = ["pizza","sauerkraut","paella","hamburger"]
countries = ["Italy","Germany","Spain","USA"]
country_specialities = zip(countries,dishes)
# print country_specialities
country_specialities_dict = dict(country_specialities)
print country_specialities_dict
