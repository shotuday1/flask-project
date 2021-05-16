print("uday")
try:
    Count = 1
    a = int(input("Enter Value"))
    print("Enter numeric value only")
    success = False
    while not success:
        if Count == "1":
            success = True
        else:
            print("Goodbye")
    print("thanks!")
except ValueError:
    b = int(input("Enter Value"))
c = a + b
print(c)
print(c, a, c + a)

print(type(c))
a = int(a)
b = int(b)
c = a + b
print(type(c))
print(c)
