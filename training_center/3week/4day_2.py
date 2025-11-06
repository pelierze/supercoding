"""
주어진 파일 이름의 파일을 읽고, 파일의 내용을 출력합니다.
파일이 존재하지 않으면 오류 메시지를 출력합니다.
에러 발생시 예외 처리는 하지 않아도 됩니다.

Args:
    filename: 읽을 파일의 이름 (문자열)
"""
import os

if os.path.exists("filename.txt") :
    with open ("filename.txt", "r", encoding = "UTF-8") as f :
        data = f.readlines()
        print(data)

else :
    print("파일을 찾을 수 없습니다.")