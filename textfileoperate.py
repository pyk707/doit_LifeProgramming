import os
import re   #정규표현식으로 문자열 다루기


""" #현재 위치 확인
print(os.getcwd())

#폴더 이동
#chdir의 괄호 안에 원하는 곳의 주소 복붙
print(os.chdir())

#폴더 안의 파일 확인하기
print(os.listdir()) """

#파일 열고 닫기
#open('파일 이름', 파일 열기 모드 ex) 'w')
#'w' 파일에 내용을 새로 쓸 때
#'r' 파일의 내용을 읽을 때
#'a' 파일에 내용을 추가할 때

""" f = open('test.txt', 'a')   #해당 파일을 추가 모드로 불러옴
f.write('회사에 가지 않을 날이 올까?')


f.close()
f = open('test.txt', 'r')   #해당 파일을 읽기 모드로 불러옴
print(f.read())
f.close()

#with 문으로 객체 만들지 않고 파일 불러오기

with open('test.txt', 'w') as g:
    g.write('with 문으로 써보기, 이렇게 하면 close를 안 해도 됨') """


#정규표현식으로 원하는 문자 반환하기
example = '이동민 교수님은 다음과 같이 설명했습니다(이동민, 2019). 그런데 다른 교수님은 이 문제에 대해서 다른 견해를 가지고 있었습니다(최재영, 2019). 또 다른 견해도 있었습니다(Lion, 2018)'

""" result = re.findall(r'\([A-Za-z가-힣]+, \d+\)', example)
print(result) """

#match 메서드 사용법
#re.match(패턴, 문자열)

""" print(re.match(r'교수', '겨수').group()) """
""" def refinder(pattern, script):
    if re.match(pattern, script):
        print('Match!')
    else:
        print('Not a match')

pattern = r'life'
script = 'life is good'
refinder(pattern, script) """

#중간에 있는 패턴 찾기_search 메서드
#re.search(패턴, 문자열)

""" def refinder(pattern, script):
    if re.search(pattern, script):
        print('Match!')
        print(re.search(pattern, script).group())
    else:
        print('Not a match')

pattern = r'교수'
script = example
refinder(pattern, script) """


#re.findall(패턴, 찾으려는 문자열)
#만약 문자열에 ‘\’ 문자가 있다면 파이썬은 그다음에 나오는 문자를 그대로 인식하지 않고 컴퓨터에 명령하기 위한 명령어로 인식합니다.

number = 'My number is 511223-1****** and yours is 521012-2******'
print(re.findall('\d{6}', number))  #\d{6} 숫자 6자리 반환
print()

# 숫자(\d)로 시작하고, 어떤 문자든(.) 반복(+)되며, '년'으로 끝나는 문자열을 반환하라고 명령합니다
example1 = '저는 91년에 태어났습니다. 97년에는 IMF가 있었습니다. 지금은 2020년입니다.'

print(re.findall(r'\d.+?년', example1))  #\d 숫자와 매치, .은 모든 문자, 년 글자 앞에 ?를 두어 년이 나오면 패턴 찾기 멈춤
print()

#괄호 안의 모든(.)문자
print(re.findall(r'\(.+\)', example))
print()
#닫는 괄호 앞에 ?를 달아줍니다.
print(re.findall(r'\(.+?\)', example))
print()


#re.split(패턴, 문자열)
sentence = 'I have a lovely dog, really. I am not telling a lie. What a pretty dog! I love this dog.'

print(re.split(r'[.!?]',sentence))  #
print()

data = 'a:3; b:4; c:5'
for i in re.split(r';', data):
    print(re.split(r':', i))


#re.sub(찾을 패턴, 대체할 문자, 찾을 문자열)
sentence = 'I have a lovely dog, really. I am not telling a lie. What a pretty dog! I love this dog.'

print(re.sub(r'dog', 'cat', sentence))
print(sentence)
print()

sentence1 = 'I have a lovely dog, really. I am not telling a lie'
print(re.findall(r'\w+?ly', sentence1))    #\w 공백이 아닌 문자나 숫자
print()