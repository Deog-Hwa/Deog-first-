# separator 옵션 
print('naver','com', sep = '@') # 단어 사이에 @ 넣기 

# end 옵션 
print("hi" , end = "")
print(" my name is duck")  # 단어 붙여서 쓰기 

# format 사용(d, s, f)
print("{} {}".format("drink", "coke"))

print("{:>10}".format("good")) # 왼쪽을 채움 


print("{:10}".format("good")) # 오른쪽을 채움 

print("{:$>10}".format("good")) 

print("{:^10}".format("good")) # 중앙 정렬 


print( '%06.3f' % (3.1412121212121))


# 다양한 변수 선언 
# Camel Case : numberOfCollegeGraduates - 메소드 
# Pascal Case : NumberOfCollegeGraduates - 클래스
# Snake Case : number_of_college_graduates 

# 수치 연산 함수 

x, y = divmod(100,4)
print(x,y)

# 외부 모듈 
import math 

print(math.pi)

# 이스케이프 문자 사용 
print("I'm Boy") 
print('I\'m Boy')
print('a \t  b')
print('a \"\" b')

# Raw String 
raw_s = r'D:\python\test'
print(raw_s)

str_1 = "alex! judy"
str_2 = "duck"
print("a" in str_1)


print(str_1.capitalize()) # 앞글자 대문자 변경 
print(str_2.endswith("k")) # 마지막 문자 k로 끝나니?
print(str_1.replace("ex", "exender")) # 문자 대체 
print(sorted(str_2)) # 리스트 형태로 만들고 정렬 
print(str_1.split("!")) # 배열 형태로 만들어 줌 

str_3 = "I Like Python"

print(str_3[1:8:2])

a = "z"
print(ord(a)) # 아스키 코드로

print(chr(122)) # 문자로 

# c[1:2] = ["a","b","c"] == c[1] = ["a","b","c"]

a = [1,5,8,3,9]

a.append(10) # 맨 뒤에 추가 
# a.reverse()  반대로 정렬 
a.sort()  # 오름차순 정렬
a.insert(3,12)  # 삽입 

# del a[2] 제거 
a.remove(5) # 제거 
a.pop() # 마지막 수 꺼내오기, stack 구조 
a.count(3) # 리스트에서 3의 개수가 몇 개인가? 
print(a)

# 튜플은 리스트와 비교했을 때 변경과 삭제가 안된다. 불변! 

# 팩킹 & 언팩킹 

# 팩킹
t = ('qwe', 'wer','evz','wex')

print(t[1])

# 언팩킹 
(x1, x2, x3, x4) = t 

print(x1,x2,x3,x4)

# 딕셔너리는 순서 x, 키 중복 x 

a = {"Name" : "Alex"}

b = { "Name" : "Alex",
      "Age"  : 13, 
      "stage": "True"
}

c = dict(Name = "Alex",
         Age  = 13, 
)

# print(a["Name1"]) # 존재x = 에러발생 
print(a.get("Name1")) # 존재x = None 처리 

# dict_keys, dict_values, dict_items : 반복문(__iter__)에서 사용 가능 

print(a.keys())
print(a.values())
print(a.items ())

# 집합(순서x, 중복x)

a = set([15,13,19])
b = {13,15,19}

# 부분 집합 확인 
a.issubset(b) # a가 b의 부분집합인가?
a.issuperset(b) # b가 a에 포함 되는가? 

a.add(9)

b.remove(15) # 없는 숫자를 지우면 에러가 발생함
b.discard(15) # 없는 숫자를 지우면 에러가 발생하지 않음 



city = "seoul"

if city:
    print("나는 {} 사람".format(city))

else: 
    print("나는 강릉 사람")

# 산술 > 관계 > 논리 - 계산 순서 

customer = "gold"
guest = "bronze"
people = "vip"

if customer == "gold" and guest == "bronze":
    print("pass")

if customer == "bronze" or people == "vvv":
    print("통과시켜")

else:
    print("통과시키지 마")

# 다중 조건문 
score = 90

if score >= 90: 
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("D")


# 중첩 조건문 
score = 90 
grade = "B"

if grade == "A":
    if score >= 90:
        print("장학금 100%")
    elif score >= 80:
        print("장학금 80%")
    else:
        print("장학금 50%")
else:
    print("장학금 없음")
# for문 
for a in range(1,10):
    print(a)

for b in range(1,10,2):
    print(b)

sum = 0 

for a in range(1,1001):
    sum += a
print(sum)

# 문자열, 리스트, 튜플, 집합, 사전 
# iterable 리턴 함수: range, reversed, enumerate, filter, map, zip 


a = {"name" : "alex", "age" : 18}

for n in a.values():
    print(n)

name = 'Manchester United'
for soccer in name:
    if name.isupper():
        print(soccer)
    else:
        print(soccer.upper())


a = [10,210,60,56,78]
for num in a: 
    if num == 60:
        print("나왔음")
        break
    else: 
        print("나오지 않았음") 
   

sports = ["soocer", "football","baseball","basketball"]

for a in sports: 
    if a == "baseball":
        continue
    else:
        print("내가 가장 좋아하는 스포츠는 {}".format(a))

sports = ["soocer", "football","baseball","basketball"]

for a in sports:
    if a == "judo":
        print("내가 싫어하는 스포츠는 {}".format(a))
        break 
else: 
    print("나는 야구를 싫어한다.")


for a in range(2,10):
    for b in range(1,10):
        print("{:4d}".format(a * b), end = '')
    print()
    

n = 12
# while n > 0:
#     n -= 1 
#     if n == 9:
#         break
#     print(n)



while n > 0:
    n -= 1 
    if n == 9:
        continue
    print(n)
        
    
def a(w):
    print("나는 맨유팬이다.",w)

word = "축구를 좋아한다."
a(word)



def mul(x):
    x1 = x * 10 
    y1 = x * 20 
    z1 = x * 30 
    return x1, y1, z1

x1, y1, z1 = mul(10)

print(x1,y1,z1)



# 일반적 함수 
def mul_func(x,y):
    return x, y 
# 이거 두개는 같은 의미 

# 람다 함수  
lambda x,y: x * y

def func_final(x, y, func):
    print(x * y * func(100,100))

func_final(10, 20,lambda x,y: x * y)


def plus(x,y):
    print(x + y)


a = plus(10,20)

print(a)


def minus(x, y):
    return x - y

print(minus(30,20))
 
# input 기본 타입은 str형 

# a = print("{0}이 성이고 {1}가 별명이다".format(input("나의 성은"), input("나의 별명은")))
# 네임스페이스 - 객체를 인스턴스화 할 때 저장된 공간 
# 클래스 변수 - 직접 접근 가능, 공유 
# 인스턴스 변수 - 객체마다 별도 존재 
class Dog2:
    # 클래스 속성
    species = "firstdog"
    # 초기화 / 인스턴스 속성 
    def __init__(self, name, age):
        self.name = name
        self.age = age

print(Dog2)

a = Dog2("minmiddle",15)
b = Dog2("zzang",14)

print( "{}의 나이는 {}이고 {}의 나이는 {}이다.".format(a.name, a.age, b.name,b.age))

print(Dog2.species)

class SelfTest:
    def func1():
        print("Func1 called")
    def func2(self):
        print("Func2 called")


f = SelfTest()

f.func2() # 인스턴스 메소드 
SelfTest.func2(f)
SelfTest.func1() # 클래스 메소드 

class Warehouse:
    stock_num = 0 # 재고 

    def __init__(self,name):
        self.name = name 
        Warehouse.stock_num += 1 
    
    def __del__(self):
        Warehouse.stock_num -= 1 

user1 = Warehouse("Lee")
user2 = Warehouse("Cho")

print(Warehouse.stock_num)
del user1 
print(Warehouse.stock_num)

class Dog:
    # 클래스 속성
    species = "firstdog"
    # 초기화 / 인스턴스 속성 
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        return '{} is {} years old'.format(self.name, self.age)

    def speak(self, sound):
        return '{} says {}!'.format(self.name, sound)


# 인스턴스 생성
c = Dog('zzang', 14)
d = Dog("minmiddle", 15)

# 메소드 호출 
print(c.info())

print(c.speak("왕왕"))



import qw

qw.add(5,4)


# SyntaxError, TypeError, NameError,IndexError, ValueError, KeyError 
# 문법적으로는 예외가 없지만, 코드 실행 프로세스 발생하는 예외도 중요 
# 1. 예외는 반드시 처리 
# 2. 로그는 반드시 남긴다. 
# 3. 예외는 던져진다.
# 4. 예외 무시 

# 예외 없는 것을 가정하고 프로그램 작성 -> 런타임 예외 발생 시 예외 처리 권장 

# AttributeError : 모듈, 클래스에 있는 잘못된 속성 사용 예외 

name = ["Kim", "Lee", "Park"]

try:
    z = "Kim"
    x = name.index(z)
    print("{} Found it! {} in name".format(z, x + 1))
except ValueError:
    print("Not found it! - Occurred ValueError!")
else:
    print("OK! else")
finally:
    print("나는 무조건 나옴")

# else문은 예외가 발생하지 않아야 실행됨 
# finally문은 예외가 발생해도 실행됨

try:
    a = 505
    if a <= 500:
        print("OK! Pass")
    else:
        raise TypeError
except TypeError:
    print("에러가 발생했습니다")
else:
    print("통과입니다.")      


import os 
print(os.environ["USERNAME"])
print(os.getcwd())

import time 
print(time.ctime())
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())))

import random
print(random.randint(1,45))

a = [1,2,3,4,5]
random.shuffle(a)
print(a)

import webbrowser
webbrowser.open("www.naver.com")


