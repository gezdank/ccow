sen = input("Enter a sentence: ")
new_sen = ""

for i in range(len(sen)):
    new_sen = sen[i] + new_sen


print(new_sen)
