# Quiz) 사이트별로 비밀번호를 만들어주는 프로그램을 작성하시오.

# 예) http://naver.com
# 규칙1: http:// 부분은 제외 => naver.com 
# 규칙2: 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙3: 남은 글자 중 처음 세자리 + 규칙2 글자 갯수 + 규칙2 글자내 'e'개수 + "!"로 구성

# 예: nav51!

site = "http://google.com"

rule_1 = site.replace("http://","")     # https인 경우 성립되지 않음
rule_2 = rule_1[:rule_1.index(".")]     # rule_1[:-4]로 하면 ".com" 말고 ".or.kr"의 경우 성립되지 않음

password = rule_2[:3] + str(len(rule_2)) + str(rule_2.count("e")) + "!"    # [len()]과 [변수.count()]는 숫자이므로 문자로 변환하여 출력해준다.
print(password)
print("{}의 비밀번호는 {}입니다." .format(site, password))


site = "http://daum.net"

rule_1 = site[site.index("/")+2:]      # https이라도 성립 가능!
rule_2 = rule_1[:rule_1.index(".")]    

password = rule_2[:3] + str(len(rule_2)) + str(rule_2.count("e")) + "!"
print("%s의 비밀번호는 %s입니다." %(site, password))



# index 공부
# test = "%s의 비밀번호는 %s입니다." %(site, password)
# index = test.index("t")
# print(index)
# index = test.index("t",index+1)                      # 앞에서 index에 대해 정의를 하지 않으면 두번째 t의 위치를 바로 알 수 없는건가?
# print(index)

