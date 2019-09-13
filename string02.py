name = input("Enter your first name: ")
new_name = ""

for ch in range(len(name)):
    new_name = new_name + name[ch] + "\n"

print(new_name)


