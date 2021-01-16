import numpy as np

print(np.zeros((2,10)))    #2행 10열의 각 원소가 0
print(np.ones((3,10)))
print(np.arange(2,10))   #2이상 10미만의 원소로 이루어진 1차원 배열

a = np.ones((2,4))
print(a)
print(np.transpose(a))    #행과 열을 바꿈

#배열 사칙연산 가능_각 자리 원소끼리 / 행과 열이 모두 다르면 안 됨

arr1 = np.array([[2,3,4],
[6,7,8]])
print(arr1.shape)
arr3 = np.array([100,200,300])
print(arr3.shape)
print()

print(arr1 + arr3)