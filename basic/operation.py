# 연산, 연산자
# 1. 산술연산자 (+, -, *, /, //, **, %)
# / : 나머지도 나누기
# // : 몫만 (java / 같은 개념)
a, b = 5, 3
# 8 2 15 1.6666666666666667 1 125 2
print(a+b, a-b, a*b, a/b, a//b, a**b, a%b)

# 문자열 연결 : +
s1, s2, s3 = "100", "100.123", "1234567"
print(s1 + s2 + s3) # 100100.1231234567

# 문자열 + 정수 : 파이썬에서는 오류 발생
print(s1 + str(1)) # 1001

# 복합대입연산자
a = 10
a += 5 # a = a + 5
print(a) # 15
a -= 5
print(a) # 10
a *= 5
print(a) # 50
a /= 5
print(a) # 10.0
a //= 5 
print(a) # 2.0
a %= 5
print(a) # 2.0

# [실습] 7,777원을 가지고 있다. 동전으로 교환하기
# 500 : 15개, 100원 : 2개, 50원 1개, 10원 2개, 나머지 돈: 7원
money = 7777
c500, c100, c50, c10 = 0, 0, 0, 0

c500 = money // 500
money %= 500

c100 = money // 100
money %= 100

c50 = money // 50
money %= 50

c10 = money // 10
money %= 10

print("500원 : %d 개" % c500)
print("100원 : %d 개" % c100)
print("50원 : %d 개" % c50)
print("10원 : %d 개" % c10)
print("나머지 돈 : %d 원" % money)

# 관계(비교)연산자 : 결과가 True, False
a, b = 10, 0
print("a == b", (a == b)) # False
print("a != b", (a != b)) # True
print("a >= b", (a >= b)) # True
print("a <= b", (a <= b)) # False

# 논리 연산자 : and, or, not
# and : &&, or : ||, not : ! (java, js)
a, b, c = 100, 60, 15
print("a > b and b > c", a > b and b > c) # True
print("a > b or b < c", a > b or b < c) # True
print("not False", not False) # True
print("not b < c", not b < c) # True


