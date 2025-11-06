# 문제 3: 리스트를 입력받아 짝수만 포함하는 새로운 리스트를 반환하는 함수를 작성하세요.

def even_numbers(numbers):
  # 여기에 코드를 작성하세요
    even_list = []
    for a in numbers :
        if a%2 == 0 :
            even_list.append(a)
    return even_list

# 아래는 수정하지 마세요.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_list = even_numbers(numbers)

print(f"짝수 리스트: {even_list}")