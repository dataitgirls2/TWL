## **스크래치 발표**

## **피드백**
- 랜덤 비슷한 건 만들 수 있음
- 직관과 데이터의 조화! 어떤 데이터를 어떻게 수집할지는 직관이 중요!
- 프로그래밍은 비안적, 처음에는 어렵거나 막히는데 좌절하지 않고 꾸준히 하기. 수업 난이도를 조절
- 프로그램 설치는 git이 가장 어려웠으므로 크게 걱정 X
- 갈아넣기 : 너무 재미있어서 열심히 하는 것

데이터 수집, 분석, 실제 웹 서비스에 연동하는 과정을 모두 한 언어에서 끝내기
문법, 성능, 지원 좋음. 훌륭한 개발자 커뮤니티, 풍부한 참고자료
분야에 따라 파이썬과 R은 사람이 파악할 만큼 속도 차이가 남

## **Blockly**


## **파이썬 시작**
http://www.pythontutor.com/live.html#mode=edit
colab 활용하기

>n = 0
>
>total = 0
>for i in range()
>total = total+i
>n = n+1
>average = total /n
>print(average)

render all objects on the heap(Python)으로 세팅하기!
모든 literal은 수식!
0xF = 15
=의 오른쪽에 나오는 식을 평가하고 결과를 =  오른쪽 변수에 넣기
for i in range(100): [0,1,2,3,4] <- 0은 literal
코딩 컨벤션 : 스페이스 4개로 들여쓰기하기, n = 0
부동소숫점 float형 2.0

fact가 거짓말을 할 가능성이 존재
범죄 통계

마크다운에서 $$으로  수식을 씌우면 표시 가능

## **기본 프로그래밍 연습**
n = 0
total = 0
for i in range(100):
    total = total +i
    n = n+1
    average = total /n
print(average)

### **함수 연습**
def calc_sum(numbs):
    result = 0
    for num in numbs:
        result = result +num
    return result

def calc_len(numbs):
    result = 0
    for num in numbs:
        result = result+1
    return result
    
def calc_average(numbs):
    total = calc_sum(numbs)
    length = calc_len(numbs)
    return total / length

scores = [50,60,70]
total = calc_sum(scores)
average = calc_average(scores)
print(total)
print(average)
