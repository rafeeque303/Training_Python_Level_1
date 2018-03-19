x = int(input("Enter a number :"))
if x%2==0:
    print(str(x)+  " is an even number..!")
else:
    print(str(x)+  " is an odd number..!")
if x%4==0:
    print(str(x)+ " is also a multiple of 4")
num = int(input("Enter a number(num) :"))
if num==0:

    num =int(input("Number can't be zero \nEnter a non zero number"))
check = int(input("Enter another number(check) :"))
if check%num==0:
    print("check can divide 'num' evenly")
else:print("check can't divide'num' evenly")











