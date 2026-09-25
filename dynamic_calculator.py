def calculate(*numbers,operation):
    if operation=="+":
        result=0
        for i in numbers:
            result+=i

    elif operation=="-":
        result=numbers[0]
        for s in numbers[1:]:
            result-=s

    elif operation=="x":
        result=1
        for m in numbers:
            result*=m

    elif operation=="/":
        result=numbers[0]
        for d in numbers[1:]:
            result/=d

    else:
        return "invalid input"
    return result

if __name__=="main":
    values = []
    v = int(input("enter the count of values you want to calculate:"))
    for i in range(v):
        a = int(input(f"enter number {i + 1}:"))
        values.append(a)
    operator = input("enter the operation you want to apply on the values(+,-,/,x):")
    result = calculate(*values, operation=operator)
    print("result:", result)



