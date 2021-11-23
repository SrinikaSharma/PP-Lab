num1 = int(input(" Please Enter the First Value Number 1: "))
num2 = int(input(" Please Enter the Second Value Number 2: "))

# Add Two Numbers
add = num1 + num2

# Subtracting num2 from num1
sub = num1 - num2

# Multiply num1 with num2
multi = num1 * num2

# Divide num1 by num2
div = num1 / num2

# Modulus of num1 and num2
mod = num1 % num2

# Exponent of num1 and num2
expo = num1 ** num2
print("The Sum of {0} and {1} = {2}".format(num1, num2, add))
print("The Subtraction of {0} from {1} = {2}".format(num2, num1, sub))
print("The Multiplication of {0} and {1} = {2}".format(num1, num2, multi))
print("The Division of {0} and {1} = {2}".format(num1, num2, div))
print("The Modulus of {0} and {1} = {2}".format(num1, num2, mod)) 
print("The Exponent Value of {0} and {1} = {2}".format(num1, num2, expo))


'''Output
Please Enter the First Value Number 1: 50
 Please Enter the Second Value Number 2: 10
The Sum of 50 and 10 = 60
The Subtraction of 10 from 50 = 40
The Multiplication of 50 and 10 = 500
The Division of 50 and 10 = 5.0
The Modulus of 50 and 10 = 0
The Exponent Value of 50 and 10 = 97656250000000000 '''
