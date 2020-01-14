import string
# import re


def text_analyzer(text=""):
    """
    This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text.
    """
    length = len(text)
    if length == 0:
        text = input("What is the text to analyze?\n>> ")
    uppers = 0
    lowers = 0
    puncts = 0
    spaces = 0
    for i in text:
        if i.islower():
            lowers += 1
        elif i.isupper():
            uppers += 1
        elif i.isspace():
            spaces += 1
        elif i in string.punctuation:
            puncts += 1
#     print("The text contains", length, "characters:")
#     print("-", sum(c.isupper() for c in text), "upper letters")
#     print("-", sum(c.islower() for c in text), "lower letters")
#     print("-", sum(c.isspace() for c in text), "punctuation marks")
#     print("-", sum(c in string.punctuation for c in text), "spaces")
    print("The text contains " + str(length) + " characters:")
    print("- " + str(uppers) + " upper letters")
    print("- " + str(lowers) + " lower letters")
    print("- " + str(puncts) + " punctuation marks")
    print("- " + str(spaces) + " spaces")


#     print(len(re.findall("[a-z]", text)))
#     print(len(re.findall("[" + string.punctuation + "]", text)))
