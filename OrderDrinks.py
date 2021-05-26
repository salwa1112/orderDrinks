# order details for a coffee shop
def getCupsize(cupOption):
    if cupOption == '1':
        return 'Small'
    elif cupOption == '2':
        return 'Medium'
    elif cupOption == '3':
        return 'Large'


def getDrink(optionDrink):
    if optionDrink == '1':
        return 'Decaf coffee'
    elif optionDrink == '2':
        return 'Latte'
    elif optionDrink == '3':
        return 'Black'


date = input("Please enter today's date: ")
customerName = input("Enter customer name: ")
value = 0
total = 0
openFile = open(r'orderDetails.txt', 'a+')
text = "Cha Time\n_________\nOrder Details:\n--------------\nToday's date:{0}\n ".format(
    date)
textName = "Customer's name:{0} ".format(customerName)
openFile.writelines(text)
while True:
    print('The available cup size options are:\n 1.small\n 2.medium\n 3. large')
    cupSize = input("Enter the cup size: ")
    print('The options for drinks are: \n 1. decaf coffee\n 2.latte\n 3. black')
    drinkOption = input('Enter the option for your drinks: ')
    quantity = int(input('Enter quantity: '))
    if cupSize == '1' and drinkOption == '1':
        value = 1.00
    elif cupSize == '1' and drinkOption == '2':
        value = 1.80
    elif cupSize == '1' and drinkOption == '2':
        value = 0.80
    elif cupSize == '2' and drinkOption == '1 ':
        value = 1.25
    elif cupSize == '2' and drinkOption == '2':
        value = 2.00
    elif cupSize == '2' and drinkOption == '3':
        value = 1.10
    elif cupSize == '3' and drinkOption == '1':
        value = 1.50
    elif cupSize == '3' and drinkOption == '2':
        value = 2.25
    elif cupSize == '3' and drinkOption == '3':
        value = 1.30
    price = value*quantity
    total += price
    print("Total Price: ${0}".format(total))

    text1 = "\n Cup Size: {0}\n Drinks name: {1} \n Quantity: {2} \n Price: {3}\n".format(
        getCupsize(cupSize), getDrink(drinkOption), quantity, price)
    openFile.writelines(text1)

    answer = input("Do you want to run this program again? (Y/N)")
    if answer.upper() == "Y":
        continue
    else:
        break
text2 = "\n Total Price: {0} ".format(total)
openFile.writelines(text2)

openFile.close()
