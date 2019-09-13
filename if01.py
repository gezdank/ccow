sentence = input("Enter a sentence: ")
space = 0
for character in sentence:
    if character == " ":
        space = space + 1

print(space)
