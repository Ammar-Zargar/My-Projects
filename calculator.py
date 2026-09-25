while True:

    a=int(input("enter the first number :"))
    b=int(input("enter the second number :"))
    operator=input("enter the operator :")
    Sum=a+b
    difference=a-b
    product=a*b
    division=a/b
    modulus=a%b

    if operator=="+":
        print(Sum)
        break
    elif operator=="-":
        print(difference)
        break

    elif operator=="*":
        print(product)
        break
    elif operator=="/":
        print(division)
        break
    elif operator =="%":
        print(modulus)
        break
    else:
        print("error occured")
