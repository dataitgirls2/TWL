# Statistics 1st class
## 모집단을 모두 수집 문석하는 것은 비용과 시간적으로 불가능하기 때문에 표본집단을 설정하는 것
  * 이름 나이 주소 등의 것을 변수 p라고 함
  * 그 아래의 재용들을 자료(observation) n이라고 함

## 통계의 한계 3가지
  * 표본의 결과는 정확한 결론이 아니라는 것
  * 확률이 있어야한다는 것
  * 틀릴 가능성을 내포하고 있다는 것 (신뢰구간)

## 모집단을 다 가지고 있는 것이 좋은가?
  * 변수가 많은 경우 차원의 저주에 걸릴 수 있음
### 파이썬 코드로 작성해보쟈아
    def f(x):
        result = 0.2**(1/x)
        return result

    def naming(x, n):
        keyName = x+str(n)
        return keyName

    pDict = {}

    for i in range(1,11):
         pDict[naming('x',i)] = f(i)

    print(pDict)
  * 변수가 많아지면, 밀도를 설명할 수 있는 데이터가 희학해지기 때문에 적은 데이터에 의존하여 잘못된 결론을 도출할 수도 있음
  * 이를 오버피팅이라고 함(예측력이 떨어짐)

# Git Bash 1st
## Git Bash를 다운받아 SSH 키를 등록
### GitHub에서 SSH 키를 generate한 다음, Git Bash로 GutHub의 이메일과 username, remote를 config

# 로컬 파일을 깃으로 관리하기
  * Git Bash를 실행
  * 위치로 이동 : cd C://Users/rlath/Desktop/constitution_kr
  * 해당 위치에 readme.md 파일을 만듦 : echo "# constitution_kr" >> README.md
  * 임시적인 폴더를 생성 : git init
  * 깃으로 readme.md파일을 작성 : git add README.md
  * 커밋 : git commit -m "first commit"
  * 리모트 설정 : git remote add origin git@github.com:soryeongk/constitution_kr.git
    이미 설정되어있다면 하지 않아도 됨 git remote -v를 입력해서 확인할 수 있음
  * README.md 파일을 깃헙의 constitution_kr으로 push : git push -u origin master

# 1987년 대한민국 헌법 파일 깃으로 관리하기
  * Git Bash를 실행
  * 위치로 이동 : cd C://Users/rlath/Desktop/constitution_kr
  * 임시적인 폴더를 생성 : git init
  * 깃으로 '대한민국 헌법.txt'파일을 지정 : git add '대한민국 헌법.txt'
  * 커밋 메시지를 작성하고 커밋 : git commit -m “1987년 헌법"
  * 파일을 깃헙으로 push : git push -u origin master
