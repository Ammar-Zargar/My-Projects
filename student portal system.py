while True:
    print("choose options:")
    print("1:student details.")
    print("2:student result.")
    print("3:student fee details.")
    name="ammar"
    Grade=12
    marks=98.00
    fee=12000.00
    print("enter the option:")
    option=int(input())
    if option == 1:
        print("Name:",name)
        print("grade:",Grade)
        break
    elif option==2:
        print("Name:", name)
        print("grade:", Grade)
        print("marks:",marks)
        break
    elif option==3:
        print("name:",name)
        print("grade:",Grade)
        print("fee:",fee)
        break
    elif option==4:
        break
    else:
        print("invalid option")