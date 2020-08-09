# if 조건:
#    실행명령문

weather = "비"
if weather == "비" or weather =="눈":
    print("우산 챙기기")
elif weather == "미세먼지":
    print("마스크 챙기기")
else:
    print("양산 챙기기")

'''1) if 조건과 비교 => 조건 맞으면 실행명령문 실행하여 종료.
                       조건 맞지 않으면 다음 조건(elif)과 비교
      elif 조건과 비교 => 조건 맞으면 실행명령문 실행하여 종료.
                       조건 맞지 않으면 다음 조건(else)과 비교
      else 조건: if, elif 조건 외 나머지 모든 조건
      ===> 위에서 부터 차례대로 실행된다. '''


# input을 써서 terminal에서 값 넣기
weather = input('"오늘 날씨는 어때요?"')
if weather == "비" or weather =="눈":
    print("우산 챙기기")
elif weather == "미세먼지":
    print("마스크 챙기기")
else:
    print("양산 챙기기")

'''2) input 값은 문자열로 받아들인다. '''

# input , int 함수 사용
temp = int(input('"기온은 어때요?"'))
if temp >= 30:
    print("너무 더워요.")
elif 10 <= temp < 30:
    print("괜찮은 날씨에요.")
elif 0 <= temp <10:
    print("쌀쌀해요.")
else:
    print("많이 추워요.") 


bag = ("money","laptop","umbrella")
if "laptop" in bag:
    print("go to library")
else:
    print("go home and get the laptop")

'''3) tuple에서(list도 가능) 해당 원소 있는지 판단하여 맞는 조건 실행 '''