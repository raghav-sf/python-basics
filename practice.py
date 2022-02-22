# Prgram that input three input and then find the sum as:
# sum1: sum of all the given numbers
# sum2 : sum of non-dublicate numbers
from numpy import angle


sum1 = sum2 =0

num1 = int(input("enter the first number:"))
num2 = int(input("enter the second number:"))
num3 = int(input("enter the third number:"))

sum1 = num1 + num2 + num3

if (num1 == num2):
    if (num3 != num1):
        sum2 += num3
else:
    if num3 == num1:
        sum2 += num2
    else:
        if num2 == num3:
            sum2 += num1
        else:
            sum2 += num1 + num2 + num3
        
print("the given numbers are:",num1, num2, num3)
print("the sum of the numbers are:", sum1)
print("the sum of non-dublicte number:",sum2)


# program to find the multiper of a number(divisor) out of given five numbers

num1 = int(input("enter number one:"))
num2 = int(input("enter number 2:"))
num3 = int(input("enter number three:"))
num4 = int(input("enter number four:"))
num5 = int(input("enter number five:"))
divisor = int(input("enter the divisor:"))

count = 0

remainder = num1 % divisor
if (remainder == 0):
    count += 1
remainder = num2 % divisor
if (remainder == 0):
    count +=1
remainder = num3 % divisor
if (remainder == 0):
    count += 1
remainder = num4 % divisor
if (remainder == 0):
    count += 1 
remainder = num5 % divisor
if (remainder == 0):
    count += 1

print("the number of multiple of divisor", divisor,"is/are",count)


# Program to make a calculator


# program to make a calculator

number1 = int(input("enter the first number: "))
number2 = int(input("enter the second number: "))

operator = input("Choose an operator between[+, -, x , /]: ")

result = 0

if operator == "+":
    result = number1 + number2
    
elif operator == "-":
    result = number1 - number2
    
elif operator == "x":
    result = number1 * number2
    
elif operator == "/":
    result = number1 / number2
    
else:
    print("please input the valid operator.")

print("The result between", number1 , operator, number2, "is", result)


# program to arrange the given number in ascending order

# program to arrange three number in ascending order

number1 = int(input("enter the first number"))
number2 = int(input("enter the second number"))
number3 = int(input("enter the third number"))

min= mid = max = None

if number1 > number2 and number1 > number3:
    if number2 > number3:
        min, mid, max = number3, number2 ,number1
    else:
        min, mid, max = number2, number3, number1
elif number2 > number1 and number2 > number3:
    if number1 > number3:
        min, mid, max = number3, number1 , number2
    else:
        min, mid, max = number1, number3, number2
else:
    if number1 > number2:
        min, mid, max = number2, number1, number3
    else:
        min, mid, max = number1, number2, number3

print("the ascending oreder of the given three numbers are:", min, mid, max)

# program to tell whether the user inputs the uppercase, lowercase or the digit character

# program to show whether a user inputs a uppercase or lawer case or a digit

char = input("enter the character: ")

if char >= "A" and char <= "Z":
    print("the character is uppercase character")

elif char >= "a" and char <= "z":
    print("the character is lowercase character")

elif char >= "1" and char <= "9":
    print("The character is digit")

else:
    print("The character is special character")
    

# program to reverse the number
#first we put the number and stored in the variable
#the create a reverse variable to store the reverse value later
#then run a while loop till the given number becomes 0
#then we will divide the number with 10 and then store the remainder in another variable
#then for storing remainder in reverse we have to multiply it with 10 to create a 10th position and add the last digit of original number
#then divide the number by 10 to remove the last position from it and making it one position shorter 
number = int(input("enter the number:")) 
reverse = 0
while number != 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number = number // 10
print("reverse of the number ", number, "is", reverse)

#program to generate the divisor
number = int(input("Enter the number: "))   #first store the input number in variable
for a in range(1, number + 1):              # then generate a loop for finding all the divisor
    if number % a == 0:                     # then import the condition for divisor that it should completly divided by the number
        print("the divisor is ", a)         #then print the number
else:
    print("-End-")
    
    
#program to check whether angle given by user are angle of triangle or not
angle1 = int(input("First angle of the given figure: "))
angle2 = int(input("Second angle of the given figure: "))
angle3 = int(input("Third angle of the given figure: "))
total = angle1 + angle2 + angle3
if (total == 180):
    print("Yes, they are angle of trianle")
else:
    print("No, they are not angle of triangle")
    
#program that display first ten Mersenne number(formula for this is 2^n -1)
for n in range(1,11):
    mersenne = 2 ** n -1
    print("mesenne series for first ten numbers ", mersenne)
 # modifing the above code also ahowing the prime mersenne numbers in the series
for n in range(1,11):
    mersenne = 2 ** n -1
    #  mid = int(mersenne / 2)        it is not compulsary to add mid in this you can also do it with mersenne
    
    for i in range(2, mersenne):
        if mersenne % i == 0:
             print(mersenne)
             break
    else:
        print(mersenne, "\tprime")
        
#maximum of two given numbers using functin method
def maximum(a, b):
    if a >= b:
        return a
    else:
        return b
    
a = int(input("Enter first integer:"))
b = int(input("Enter the second integer:"))
print(maximum(a, b))

# program to find simple intrest
principle = int(input("Principle: "))
time = int(input("Number of years: "))
rate = float(input("Rate of intrest in %: "))
simpleIntrest = (principle * time * rate) / 100

print("the simple intrest is, ", simpleIntrest)

# Program to find the compond intrest
principle = int(input("Principle: "))
time = int(input("Number of years: "))
rate = float(input("Rate of intrest in %: "))
amount = principle * (pow((1 + rate / 1000), time))
compoundIntrest = amount - principle
print("Compound intrest:", compoundIntrest)

# program to print all prime numbers in a given series
start = int(input("starting number of the series: "))
end = int(input("Last number of the series: "))
for i in range(start, end + 1):
    if i > 1:
        for j in range(2, i):
            if (i % j == 0):
                break
            else:
                print(i)
                
                
    
    