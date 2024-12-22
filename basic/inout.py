# 화면 입출력
print("T", "E", "S", "T") # T E S T
print("T", "E", "S", "T", sep = "") # TEST

# 엔터 없애기 end
print("Life is too short", end=" ") 
print("You need Python")

# sep 추가
print("2024", "12", "20", sep = "-") # 2024-12-20

# 문자열 포멧팅
# %d : 정수, %f : 부동소수, %c : 문자 1개, %s : 문자열 (+ 어떤 형태의 값도 가능)
# %% : % 라는 문자
# I eat 3 apples
apple = 3
print("I eat", apple, "apples") # I eat 3 apples
print("I eat %d apples" % apple) # I eat 3 apples

msg = "I eat %d apples" % apple # I eat 3 apples
print(msg)

msg = "I eat %s apples" % apple # I eat 3 apples
print(msg)

print("Error is %d%%" % 98) # Error is 98%

number = 10
day = "three"
msg = "I ate %d apples, so I was sick for %s days" % (number, day) # I ate 10 apples, so I was sick for three days
print(msg)

# 포맷코드와 숫자 함께 사용
"""
hi
        hi
hi        jane
"""
print("%s" % "hi")
print("%10s" % "hi") # (hi에 대한것)전체 길이가 10이고 오른쪽 정렬하고 나머지는 공백
print("%-10sjane" % "hi") # (hi에 대한것)전체 길이가 10이고 왼왼쪽 정렬 후 나머지는 공백

# 소수점 4번쨰 자리까지 출력
# 0 : 길이에 상관하지 않음
# 10 : 소수점을 포함해서 10자리를 사용, 오른쪽 정렬
print("%0.4f" % 3.141592152) #3.1416
print("%10.4f" % 3.141592152) #    3.1416

# "".format()
msg = "I eat {} apples".format(apple) # I eat 3 apples
print(msg)

msg = "I ate {} apples, so I was sick for {} days".format(number, day)
print(msg) # I ate 10 apples, so I was sick for three days

# f 문자열 포멧팅
msg = f"I ate {number} apples, so I was sick for {day} days"
print(msg) # I ate 10 apples, so I was sick for three days

# # 키보드 입력
# # input()
# print("숫자 입력")
# msg = input()
# print(msg)

# msg = input("숫자 입력 : ")
# print(msg)

# 숫자 2개를 입력받은 후 연산 프로그램 작성
num1 = int(input("첫번째 수 : "))
num2 = int(input("두번째 수 : "))
print(num1 + num2)