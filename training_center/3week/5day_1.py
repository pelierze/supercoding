#[예외처리] 사수 도움 요청 업무①
 
import os

# 파일 입출력 연습문제 1: 파일 생성 및 쓰기

def create_and_write_file(filename, content):
    """
    주어진 파일 이름으로 파일을 생성하고, 주어진 내용을 파일에 씁니다.
    만약 파일이 이미 존재한다면, 기존 내용을 덮어씁니다.
    try - except - else 를 사용하세요.

    에러가 발생시:
        f"파일 '{filename}'이 성공적으로 생성 및 쓰기 실패하였습니다."
    성공시:
        f"파일 '{filename}'이 성공적으로 생성 및 쓰기 완료되었습니다."

    Args:
        filename: 생성할 파일의 이름 (문자열)
        content: 파일에 쓸 내용 (문자열)
    """
    





# 파일 입출력 연습문제 2: 파일 읽기 및 내용 출력

def read_and_print_file(filename):
    """
    주어진 파일 이름의 파일을 읽고, 파일의 내용을 출력합니다.
    파일이 존재하지 않거나 다른 오류가 발생하면 오류 메시지를 출력합니다.
    os.path.exists() 함수를 사용하지 않고 try - except 를 사용하세요.

    Args:
        filename: 읽을 파일의 이름 (문자열)
    """



# 파일 입출력 연습문제 3: 파일 추가 쓰기

def append_to_file(filename, content):
    """
    주어진 파일 이름의 파일의 끝에 주어진 내용을 추가합니다.
    파일이 존재하지 않으면 새 파일을 생성하고 내용을 씁니다.
    try - except 를 사용하세요.
    예외가 발생하면 아무것도 하지 않습니다.

    Args:
        filename: 추가 쓸 파일의 이름 (문자열)
        content: 파일에 추가할 내용 (문자열)
    """




# 파일 입출력 연습문제 4: 파일에서 특정 줄 읽기

def read_specific_line(filename, line_number):
    """
    주어진 파일에서 특정 줄을 읽어서 반환합니다.
    파일이 없으면 "파일이 존재하지 않습니다."를 출력합니다.
    line_number가 유효하지 않으면 "유효하지 않은 줄 번호입니다."를 출력합니다.
    os.path.exists() 와 len() 함수를 사용하지 마시고,
    try - except 와 FileNotFoundError 와 IndexError 를 사용하여 처리하세요.
    이외의 에러가 발생하면 "오류 발생: {에러 메시지}"를 출력합니다.
    오류가 발생하면 모든 경우에 None 값을 반환 합니다.

    Args:
      filename: 파일 이름 (문자열)
      line_number: 읽을 줄 번호 (정수, 1부터 시작)
    """