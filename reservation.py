"""reservation 코드를 while 문으로 계속 해서 반복 하도록 한다.
이름에 "대기자" 라고 쓰면, 현재 대기자 명단을 출력 한다.
이름에 "예약자" 라고 쓰면, 현재 예약자 명단을 출력 한다.
예약자가 오면, "XXX님 테이블로 안내해드리겠습니다"라고 안내를 한 후에 예약자 명단에서 삭제한다.
예약을 안한 사람이 오면, "XXX님 기다려 주세요"라고 안내를 한 후에 대기자 명단에 추가 한다.
이름에 "예약 이름" (예 "예약 홍길동") 이렇게 쓰면
먼저 홍길동이 대기자 명단에 있는지 확인하고 있을 경우 "홍길동님 테이블로 안내해 드리겠습니다"라고 안내를 하고 
홍길동을 대기자 명단에서 삭제한다.
홍길동이 대기자 명단에 없으면 예약자 명단에 홍길동을 추가한다.
대기자와 예약자는 중복된 이름이 들어가지 않도록 한다.
이름에 "종료"를 입력하면 현재 대기자와 예약자 명단을 출력하고 프로그램을 끝낸다."""


reservation_list = []
waiting_list = []

while True:
        name = input("이름을 입력해 주세요 :")

        if name == "종료" :
                print(reservation_list)
                print(waiting_list)
                break
        elif name == "대기자" :
               print(waiting_list)
        elif name == "예약자" :
               print(reservation_list)
        elif name[:2] == "예약" :
                name_temp = name[3:]
                if name_temp in waiting_list :
                        print (f"{name_temp}님 테이블로 안내해드리겠습니다.")
                        reservation_list.remove(name_temp)
                elif name_temp not in waiting_list :
                        if name_temp not in reservation_list :
                            reservation_list.append(name_temp)
                            print (f"{name_temp}님 대기자 명단에 추가했습니다 기다려주세요.")
        elif name in reservation_list :
            print (f"{name}님 테이블로 안내해드리겠습니다.")
            reservation_list.remove(name)
        elif name not in reservation_list :
                print (f"{name}님 기다려 주세요")
                if name not in waiting_list :
                    waiting_list.append(name)