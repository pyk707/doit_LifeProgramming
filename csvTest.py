import csv, os


##CSV
#CSV는 콤마로 이루어진 파일임
#파이썬에서 사용하려면 CSV 파일 가공이 필요
#CSV형 리스트 = [[1행], [2행], …, [n행]]
#CSV 파일을 파이썬으로 불러오는 것을 ‘읽다(read)’라고 하고, 
#파이썬으로 가공한 파일을 CSV 파일로 저장하는 것을 ‘쓰다(write)’라고 표현합니다.

os.chdir(r'C:\Users\pyk70\OneDrive\@coding\python\doit_LifeProgramming\doit_LifeProgramming')
f = open('a.csv', 'r', encoding='utf-8')

#CSV파일을 저장한 객체를 파이썬으로 읽으려면 csv.reader로 읽어와야 함
new = csv.reader(f)
print(new)
print()

for i in new:
    print(i)

#앞에서 csv.reader(f)로 a.csv 파일을 읽은 값을 new 객체에 저장하면서 커서가 맨 마지막으로 이동했기 때문입니다.
#다시 파일을 처음부터 읽기 위해서는 seek() 함수를 사용해 커서를 처음으로 이동해야 합니다.
f.seek(0)

a_list = []
for i in new:
    print(i)
    a_list.append(i)



def opencsv(filename):
    f = open(filename, 'r')
    reader = csv.reader(f)
    output = []
    for i in reader:
        output.append(i)
    return output