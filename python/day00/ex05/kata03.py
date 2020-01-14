def rightminus42(phrase):
    print(f"{phrase:->42}", end="")
    # print("{:->42s}".format(phrase), end = "")


phrase = "The right format"
rightminus42(phrase)
