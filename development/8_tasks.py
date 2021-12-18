###1 반환값이 있는 함수
def cir_area(r):
    return r**2 * 3.14

def cir_circum(r):
    return 2*3.14*r

r = float(input("반지름을 입력하세요 : "))
area = cir_area(r)
circum = cir_circum(r)

print('원의 면적 : %.2f, 원주율 길이 : %.2f' %(area,circum))


###2. 반환 값이 여러개인 함수

def circle(r):
    return (r**2 * 3.14,2*3.14*r)

r = float(input("반지름을 입력하세요 : "))
area,circum = circle(r)
print('원의 면적 : %.2f, 원주율 길이 : %.2f' %(area,circum))


### 3.빈도수 구하는 함수

def count(list,mscore=0,y=100):
    cnt = 0
    for i in list:
        if i >=mscore and i<y:
            cnt+=1
    return cnt

L = [95,93,87,63,95,70,60,75,88]

print("90이상 100미만 : %d명 "%count(L,90))
print("80이상 90미만 : %d명 "%count(L,80,90))
print("70이상 80미만 : %d명 "%count(L,70,80))
print("70미만 : %d명 "%count(L,y=70))

###4. 평균함수 정의하기

def f_avg(list_or_dict):
    sum=0
    for i in list_or_dict:
        sum += i
    return sum/len(list_or_dict)



s1 = [95,99,75,85]
s2 = [88,66,95,90]
s3 = [80,90,100,85]
s4 = [99,85,67,99]
s5 = [95,95,100,90]
score = [s1,s2,s3,s4,s5]

sc_sbject ={"국어" : [95,88,80,99,95], "영어" : [99,66,90,85,95], "수학" : [75,95,100,76,100],"과학" : [85,90,85,99,90]}

print("==== 평균 ====")
for i in range(5):
    print("학생%d : %.2f"%(i+1,f_avg(score[i])))

print("==== 과목별 평균 ====")
for i in sc_sbject.keys():
    print("%s : %.2f"%(i,f_avg(sc_sbject[i])))