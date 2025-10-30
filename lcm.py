A = int(input("첫번째 숫자 : "))
B = int(input("두번째 숫자 : "))
min_A = set()
min_B = set()


for i in range (1, A+1) :
    if A%i == 0 :
        min_A.add(i)

for i in range (1, B+1) :
    if B%i == 0 :
        min_B.add(i)

min_combine = min_A & min_B

gcd = max(min_combine)

lcm = A*B // gcd

print(lcm)

