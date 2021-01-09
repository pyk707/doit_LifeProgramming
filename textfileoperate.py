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

f = open('test.txt', 'a')   #해당 파일을 추가 모드로 불러옴
f.write('회사에 가지 않을 날이 올까?')
f.close()
f = open('test.txt', 'r')   #해당 파일을 읽기 모드로 불러옴
print(f.read())
f.close()

#with 문으로 객체 만들지 않고 파일 불러오기

with open('test.txt', 'w') as g:
    g.write('with 문으로 써보기, 이렇게 하면 close를 안 해도 됨')