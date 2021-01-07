##계산기 만들기


#19*19단
""" for a in range(1, 20):
    for b in range(1, 20):
        print(f"{a} x {b} = {a*b} ")
        if b == 19:
            print() """

#round(a/b, 1) 나누고 소수점 1의 자리까지만 표시


#lambda?

""" y = lambda x : 3 * x
print(y(12))
print()

x = lambda a, b : a + b
print(x(1,2))
print()

littlePrince = "여섯 살 적에 나는 라는 제목의, 원시림에 관한 책에서"
short = lambda z : z[:10]

print(short(littlePrince)) """


# def의 활용

""" def calculator(a, b):
    return a+b, a-b, a+b, a/b

print(calculator(12,3))     #튜플로 반환 """


#input 함수로 입력 받기

a=input('숫자를 하나 입력하면 짝수인지 홀수인지 구분합니다 : ')
a=float(a)
a=round(a,1) 
print(a)
type(a)


#if 함수 사용하기

def seperate():
    a=input('숫자를 하나 입력하면 짝수인지 홀수인지 구분합니다 : ')
    
    a=float(a)
    a=round(a,1) 
    print(a)
    type(a)
    
    if a % 2 == 0:
        print('입력값은 짝수ㅋ')
    else:
        print('입력값은 홀수ㅋ')

