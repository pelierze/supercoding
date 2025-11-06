# 문제 2: 문자열을 입력받아 문자열의 길이와 문자열을 역순으로 반환하는 함수를 작성하세요.

def string_info(text):
    # 여기에 코드를 작성하세요.
    len2 = len(text)
    reversed_text = text[::-1]
    # reversed_text = ""
    # for i in range(len2-1, -1, -1):
    #   reversed_text += text[i]
    return len2, reversed_text

# 아래는 수정하지 마세요.
my_string = "hello"
length, reversed_string = string_info(my_string)

print(f"문자열 길이: {length}")
print(f"역순 문자열: {reversed_string}")