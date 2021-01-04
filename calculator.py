##계산기 만들기


#19구구단
for a in range(1, 20):
    for b in range(1, 20):
        print(f"{a} x {b} = {a*b} ")
        if b == 19:
            print()