def sum(x,y):
    sum = x + y
    print("\n The sum is: " + str(sum))



def difference(x,y):
    difference = x - y
    print("\n The difference is: " + str(difference))




def product(x,y):
    product = x * y
    print("\n The product is: " + str(product))




def quotient(x,y):
    quotient= x / y
    print("\n The quotient is: " + str(quotient))




x = int(input("\n Enter the first number: "))
y = int(input("\n Enter the second number: "))




user_input = int(input("\n\n 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division \n \n Select the operation to perform:  "))




if user_input == 1:
    sum(x,y)

elif user_input == 2:
    difference(x,y)

elif user_input == 3:
    product(x,y)

elif user_input == 4:
    quotient(x,y)


