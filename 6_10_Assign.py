a = int(input("Please enter a number: "))
b = int(input("Please enter a number: "))
c = int(input("Please enter a number: "))
print(a)
print(b)
print(c)
if (a > b and a > c):
    print("a is grater number", a)
elif (b > a and b > c):
    print("b is grater number", b)
else:
    print("c is grater number", c)