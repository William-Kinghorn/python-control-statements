# welcome user 

print("welcome.")
print("In this program we will assess")
print("the equality of three numbers.")
print("You will be asked for three numbers,")
print("which this program will then use")
print("to decide equality")

# prompt user to input three numbers

x = input("Enter first number...")
y = input("Enter second number...")
z = input("Enter third number...")   

if x == y and y == z:
        print("All Numbers are Equal to Each Other")
elif x != y and y != z:
        print("All Numbers Are Not Equal To Each Other")
else:
        print("Some Numbers Are Equal But Not All Of Them")    
