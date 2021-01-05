##계산기 만들기


#19*19단
""" for a in range(1, 20):
    for b in range(1, 20):
        print(f"{a} x {b} = {a*b} ")
        if b == 19:
            print() """

#round(a/b, 1) 나누고 소수점 1의 자리까지만 표시

#lambda?

y = lambda x : 3 * x
print(y(12))
print()

x = lambda a, b : a + b
print(x(1,2))
print()

littlePrince = "여섯 살 적에 나는 '체험한 이야기'라는 제목의, 원시림에 관한 책에서"
short = lambda z : z[:10]

short(littlePrince)