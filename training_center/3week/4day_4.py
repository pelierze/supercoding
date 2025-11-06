"""
[파일입출력] 사수 도움 요청 업무④
 
주어진 파일에서 특정 줄을 읽어서 반환합니다.
파일이 없으면 오류 메시지를 출력합니다.
line_number가 유효하지 않으면 오류 메시지를 출력합니다.
오류가 발생하면 None 값을 반환 합니다.

Args:
  filename: 파일 이름 (문자열)
  line_number: 읽을 줄 번호 (정수, 1부터 시작)
"""
import os
def read_return (filename, line_number) :
    if not os.path.exists(filename) :
        print(f"{filename}을 찾을 수 없습니다.")
        return None
    try :
        with open (filename, "r", encoding = "utf-8") as f :
            lines = f.readlines()
            if 1 <= line_number <= len(lines) :
                return lines[line_number-1].rstrip("\n")
            else :
                print(f"{line_number}에 해당하는 줄이 없습니다.")
    except Exception as e:
        print(f"오류 발생{e} ")
        return None
    

