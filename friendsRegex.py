import os, re, codecs

#friends101.txt 파일을 저장한 폴더로 이동합니다
os.chdir(r'C:\Users\pyk70\OneDrive\@coding\python\doit_LifeProgramming\doit_LifeProgramming')

#코덱 오류 방지를 위해 codecs를 사용해 텍스트 파일을 불러와 객체 f에 저장
#불러오는 방식은 utf-8, f를 읽기 모드로 열어 script101이라는 객체에 저장
#이러면 f를 일일이 불러오지 않고 script101을 바로 사용하면 됨
f = codecs.open('friends101.txt', 'r', encoding = 'utf-8')
script101 = f.read()

#이상이 없는지 script101를 슬라이싱해서 확인
""" print(script101[:100]) """

#'Monica:' 다음 아무 문자나 반복되는 '.+' 패턴 모두 저장
#모니카 대사 출력
Line = re.findall(r'Monica:.+', script101)

#모니카 대사 이쁘게 출력하기
for i in Line[:]:
    print(i)

f.close()

#모니카 대사를 txt파일로 저장하기
f = open('monica.txt', 'w', encoding = 'utf-8')

monica = ''

for i in Line:
    monica += i

f.write(monica)
f.close



#등장인물 리스트 만들기
#규칙은 '대문자 + 소문자 + :'
char = (r'[A-Z][a-z]+:') 

#등장인물 중복됨
characters = re.findall(char, script101)

#set으로 중복된 원소 지우고 리스트로 변환
characters_set = list(set(characters))
print(characters_set)

#[:-1]로 ':'지우기
#우선 characters_set_sub를 리스트를 담을 변수로 선언한다
characters_set_sub = []

for i in characters_set:
    characters_set_sub += [i[:-1]]

print(characters_set_sub)


