# Multiples of 3 but not multiple of 5: 
# Write a program that prints the numbers that are 
# between 1 to 100 and multiples of three but not divisible 5

i = int(input("enter num :"))

if(1<=i<=100 and i%3==0 and i%5!=0):
    print("true")
else:
    print("false")  