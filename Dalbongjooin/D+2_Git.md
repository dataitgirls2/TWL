###Title
  #1 용어
  #2 "헌법개정안"실습 : Git bash로 '내 로컬'과 'Git' 연결 하기
  #3 "2018년 헌법 개정안"실습 : branch 이해하기 

##1 용어
  * Git init
      '내 로컬'(저장소)를 초기화 한다
  * Add
      'Stage'상태로 보낸다
      '내 로컬'에서 변경 된 이력을 인덱스에 추가 할 것을 요청 하는 과정 
  * Commit
    add 된  '인덱스'파일을 push 하기 전 확인 '도장'을 찍어주는 것과 같은 최종적인 승인 과정
  * Push(업로드)
      '내 로컬'에서 Add 된 내용을 '원격 저장소'공유할 때 요청 하는 과정    
  * Clone
      저장소를 복사
  * Git Bash 
      '터미널' 
      '내 로컬'의 디렉토리에 변경된 내용을 'Git Bash'를 통해 직접 업로드 하는 곳
  * cd : change directoy
  * ;q 나가기 ,;w 저장하기  ;wq 저장하고 나가기
  * -u : upstream
    -f : 강제로 push 하는 명령어
  * branch 
    origin : 원격 저장소 (GitHub)
    master : '내 로컬' 
  
##2 "헌법개정안"실습 : Git bash로 '내 로컬'과 'Git' 연동 준비 단계

>'내 로컬'과 GitHub 연동시키기 
> 로컬과 원격 저장소에 관리할 저장소, 파일 지정하기

# git init -> git add -> git commit -> git push

>git init, git add, git commit 까지<

  1.파일 다운로드 
     원본 파일 (1987 년 헌법개정안) 다운로드
    
  2.Git으로 관리 할 폴더 생성 (constitution-kr)
  
  4.git init 
  
  5.git add "대한민국 헌법.txt" 
     버전 관리 될 파일 명을 입력
     
  6.git commit -m "1987년 헌법" 
    * -m : message를 의미 한다. 
      GitHub에 어떤 message로 commit 할 것인지 지정 해주는 것 
    * 옵션에 대한 도움말 은 git commit -h 를 통해 볼수 있다.
      
  7.git remote add origin " 내 GitHub repository 주소" 
    '원격 저장소'를 지정
    * 이 때, git config --list 를 통해 내 원격 저장소 주소를 확인하면 "https"인지 "ssh" 인지 확인가능 
      만약 https 라면 GitHub 의 setting 에서 SSH key를 재등록 해야함 
      
  8.git push -u origin master
    '내 로컬'의 파일을 GitHub으로 관리 할 수 있게 push 하는 과정 
  
  ##3 "2018년 헌법 개정안"실습 : branch 이해 하기
    수정 사항을 업데이트 한다 =  master branch 라는 큰 흐름 속 에 '수정 branch'를 추가 해 가는 것이다.  
    
    >branch 생성 & 파일을 branch에 push 하는 과정
    1. git checkout -b 2018  *"" 추가 안한다 <br>
      2018 이라는 branch 생성
     
    2. git checkout (이동하고자 하는 branch 명) 
      ex) git checkout 2018
    
    3. git add "대한민국 헌법. txt" 
      파일을 stage 상태로 보낸다
    
    4.git commit -m"2018년 개정안" 
    
    5.git push -u origin 2018(업데이트 하고 싶은 브랜치 명을 입력 한 것이다)
    
    >GitHub에서 브랜치 바꾸기 
    6.GitHub에서 2018 -> master 로 pull request 요청
    
  
