names = ["Amal" , "Mohammed", "Khadijah", "Abdullah", "Rawan", "Faisal", "Layla"]
numbers = ['1111111111, 2222222222, 3333333333, 4444444444, 5555555555, 6666666666, 7777777777']

names.append('')
numbers.append('')

First_Person = {'name': 'Amal', 'number_is': '1111111111'}
Second_Person = {'name': 'Mohammed', 'number_is': '2222222222'}
Third_Person = {'name': 'Khadijah', 'number_is': '3333333333'}
Fourth_Person = {'name': 'Abdullah', 'number_is': '4444444444'}
Fifth_Person = {'name': 'Rawan', 'number_is': '5555555555'}
Sixth_Person = {'name': 'Faisal', 'number_is': '6666666666'}
Seventh_Person = {'name': 'Layla', 'number_is': '7777777777'}

number = input("Enter The Number:  ")

if number == "1111111111":
    print("Amal")

elif number == "2222222222":
    print("Mohamme")

elif number == "3333333333":
    print("Khadijah")

elif number == "4444444444":
    print("Abdullah")

elif number == "5555555555":
    print("Rawan")

elif number == "6666666666":
    print("Faisal")

elif number == "7777777777":
    print("Layla")

elif number == "8888888888":
    print("Sorry, this number is not found")

elif number == "9999999999":
    print("Sorry, this number is not found")

elif number == "1234567890":
    print("Sorry, this number is not found")

else:
 print('This is invalid number')

