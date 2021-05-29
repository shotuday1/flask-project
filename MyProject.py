
print("Hello")

i=1
while i < 6:
    a = str(input("Enter Name"))
    b = str(input("Enter Password"))
    print(a)
    print(b)

    if a == "uday" and b == "pass":
        print("Right Value")
    else:
        if i >= 5:
            print("Try Again")
    i += 1
else:
    print("You have reached maximum number of attapts")