"""문제 설명
어떤 자연수 N에 대하여, N의 약수 중 1과 N을 제외한 수를 진또배기 약수라고 합니다. 
N의 진또배기 약수들이 주어질 때, N을 구하는 프로그램을 작성하시오.

입력

첫째 줄과 둘째 줄에 각각 A와 B가 주어집니다. (0<AB<50,000)
N의 진또배기 약수들이 주어진다. 진또배기 약수는 2 이상 1,000,000 이하 자연수이며, 중복되지 않는다.

출력
N을 출력합니다."""
import math

divisorlist = []

while 1:
    A = input("input number : ")
    if not A.isdigit() :
        break
    else :
        divisorlist.append(int(A))

print(divisorlist)

x = math.lcm(*divisorlist)

print(x)




