# 문제 1: 두 수를 입력받아 합, 차, 곱, 몫, 나머지를 반환하는 함수를 작성하세요.

def calculate(num1, num2):
    # 여기에 코드를 작성하세요.]
    sum = num1 + num2
    diff = num1 - num2
    mul = num1 * num2
    d = num1 // num2
    r =  num1 % num2
    return sum, diff, mul, d, r

# 아래는 수정하지 마세요.
num1 = 10
num2 = 3
sum_result, sub_result, mul_result, div_result, mod_result = calculate(num1, num2)

print(f"{num1} + {num2} = {sum_result}")
print(f"{num1} - {num2} = {sub_result}")
print(f"{num1} * {num2} = {mul_result}")
print(f"{num1} // {num2} = {div_result}")
print(f"{num1} % {num2} = {mod_result}")