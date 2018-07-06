### 0705_프로그래밍


 	넘파이 : 파이썬을 빨리 실행 시킬 수있는 라이브러리 



1.함수와 이름공간 복습

	datum : data 단수 형 

	return 반환하다. 

	

#재귀적 결합 





- sorted : 순서대로 배열 하게 한다
- zip : 여러 list를 합쳐 준다 . 
- () : tuple 

    def by_name(student):
    	reuturn student[0]
    def by_age(student):
    	return student[1]
    sorted(students, key = by_name)
    로 지정 하면 students 리스트 중 
    name의 순서대로 배열하라는 명령 
    



- Higher order ft  (ex. second order ft)
   함수를 함수의 인자로 받는 함수  (second degree polynomial ft)
  ex. sort 
   함수를 함수의 인자로 받고 그 함수를  또 함수의 인자로 받을 때 ( third degree polynomial)
  
- Lambda 
  빨리 함수를 정의하고 버리는 기능을 한다
  다시 쓸 일이 있다면 , 함수를 정의 해야함 
  sorted(students, key= lambda student, student[0])
  	   'list 이름''                          parameter, expression
- key ""  : 키워드를 입력 하겠다.
