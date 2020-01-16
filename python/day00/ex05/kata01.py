languages = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
    }

for key, val in languages.items():
    print(key, "was created by", val)

# for item in languages:
#     print("%s was created by %s" % (item, languages[item]))

# print("""Python was created by {Python}
# Ruby was created by {Ruby}
# PHP was created by {PHP}""".format(**languages)) 
