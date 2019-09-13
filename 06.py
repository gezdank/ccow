total_money = int(input("How_much_you_have? "))

number_of_ten_coins = total_money // 10
number_of_five_coins = (total_money % 10) // 5
number_of_two_coins = (total_money % 10) % 5 // 2
number_of_one_coins = (total_money % 10) % 5 % 2 

print("")
print (number_of_ten_coins)
print (number_of_five_coins)
print (number_of_two_coins)
print (number_of_one_coins)


