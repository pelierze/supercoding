"""주어진 파일 이름으로 파일을 생성하고, 주어진 내용을 파일에 씁니다.
만약 파일이 이미 존재한다면, 기존 내용을 덮어씁니다.
에러 발생시 예외 처리는 하지 않아도 됩니다.

Args:
    filename: 생성할 파일의 이름 (문자열)
    content: 파일에 쓸 내용 (문자열) """

with open ("filename.txt", "w") as f :
    f.write("content")