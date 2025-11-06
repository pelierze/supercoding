"""
주어진 파일 이름의 파일의 끝에 주어진 내용을 추가합니다.
파일이 존재하지 않으면 새 파일을 생성하고 내용을 씁니다.

Args:
    filename: 추가 쓸 파일의 이름 (문자열)
    content: 파일에 추가할 내용 (문자열)
"""

with open ("filename.txt", "a", encoding = "UTF-8") as f :
    data = "content"
    f.wirte(data)