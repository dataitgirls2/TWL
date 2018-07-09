---
layout: post
title:Github에 블로그 만들기 (by Jekyll)
Date:2018-07-09
---

# Github에 블로그 만들기 (by Jekyll)

Jekyll(이하 지킬)을 통해 Github에 정적 블로그(HTML 웹사이트)를 만들어보자. 지킬은 루비 스크립트로 만들어져 있으나, 블로그를 만드는데에 있어 루비를 알 필요는 없다. 다음 과정은 Mac OS를 기준으로 진행된다.



## 지킬 설치

1. Mac OS는 루비가 이미 설치되어 있다.

   ~~~ 
   # ruby 버전 확인
   ruby -v
   ~~~

   

2. 지킬 설치를 위해 Xcode의 설치가 필요하다. (이미 설치되어 있다면 생략)

   ~~~
   # Xcode 설치
   xcode-select --install
   ~~~

   

3. 지킬을 설치한다.

   : 이 과정에서 permission error가 발생하면 ***sudo***를 앞에 붙여 입력한다.

   ~~~
   # jekyll 설치
   gem install jekyll
   ~~~





## 새로운 페이지 생성하기

<u>(주의)</u> 페이지 생성시에 주소는 반드시 **나의깃허브아이디**.github.com 이어야 한다.



1. 계정 주소에 알맞는 페이지를 생성한다.

   : 다음 입력을 통해 *나의깃허브아이디.github.com* 디렉토리가 만들어진다.

   ~~~
   jekyll new 나의깃허브아이디.github.com
   ~~~

   

2. 디렉토리로 이동한다

   ~~~ 
   cd ~/나의깃허브아이디.github.com
   ~~~

   

3. 서버를 구동시킨다.

   : 만약 `could not locate Gemfile` 과 같은 Gemfile Error가 발생하면 ***(sudo) bundle install*** 입력하여 bundler을 install하고 bundle로 서버를 구동시켜준다.

   ~~~
   # 테마 설치를 한번도 안했을 때
   jekyll serve --watch
   ~~~

   ~~~
   # 테마 설치를 해봤을 때
   bundle exec jekyll serve
   ~~~

   

4. 서버에서 페이지가 제대로 구동되는지 확인한다.

   : 웹브라우저 주소창에 `localhost:4000` 을 입력해보면 디폴트로 생성된 블로그를 볼 수 있다.

   <img src="/images/fulls/01.jpg" class="fit image">





## 내 깃허브에 연동시키기

<u>(주의)</u> repository 생성시에 주소는 반드시 **나의깃허브아이디**.github.com 이어야 한다.



1. 깃허브에서 ***나의깃허브아이디.github.com*** 이라는 이름으로 New repository를 생성한다.

<img src="/images/fulls/02.jpg" class="fit image">



2. repository URL을 복사한다.!	

   <img src="/images/fulls/03.jpg" class="fit image">

   

3. 터미널로 돌아가서, repository를 연결하고 push 해준다.

   : 터미널에서 현재 위치는 *~/나의깃허브아이디.github.com* 이여야 한다. 

   ~~~
   # connect repository
   git init
   git remote add origin *복사한 repository URL*
   git remote -v
   
   # commit and push
   git add .
   git commit -m "Create blog"
   git push -u origin master
   ~~~



4. 깃허브에서 commit 이 잘 되었는지 확인하고 블로그 생성을 확인한다.

   : `나의깃허브아이디.github.io` 에서 내 블로그를 볼 수 있다. 연동에는 5분 이상의 시간이 걸릴 수 있다. *(조금 기다려보자 꼭!!!!!)*





## 지킬 테마 설정하기

테마를 사용하기 위해서는 bundler 의 설치가 필요하다. 테마는 다음 사이트에서 선택할 수 있다.

> Jekyll Themes :  http://jekyllthemes.org



1. bundler를 설치한다.

   ~~~
   gem install bundler
   ~~~



2. 내가 원하는 테마를 사이트에서 고르고 파일을 다운로드 한다.

   <img src="/images/fulls/04.jpg" class="fit image">



3. 압축된 파일을 풀고, 내 *나의깃허브아이디.github.com* 디렉토리에 모두 붙여넣는다.

   : 테마를 여러번 바꾸다 보면 실수로 불필요한 파일이 남거나 덮어씌어지지 않을 수 있으니, 디렉토리를 비우고 붙여넣는 것을 추천한다.



4. 터미널로 돌아가서 빌드를 진행한다.

   : 터미널에서 현재 위치는 *~/나의깃허브아이디.github.com* 이여야 한다. 

   ~~~
   # 둘 중 하나를 이용
   bundle exec jekyll serve
   jekyll serve
   ~~~

   *(참고 1)* 만약 `could not locate Gemfile` 과 같은 Gemfile Error가 발생하면 	***(sudo) bundle install*** 를 입력하여 bundler을 install하고 bundle로 서버를 구동시켜준다.

   *(참고 2)* 루비의 버전이 문제라면 **bundle update** 를 입력하여 업데이트 해주면 된다.

   

5. 서버에서 페이지가 제대로 구동되는지 확인한다.

   : 웹브라우저 주소창에 `localhost:4000` 을 입력해보면 테마가 바뀐 블로그를 볼 수 있다. 

   <img src="/images/fulls/05.jpg" class="fit image">

   *(참고)* `localhost:4000` 을 입력했는데 404 와 같이 빈 창이 나온다면, `_config.yml` 파일을 확인해봐야 한다.

   <img src="/images/fulls/06.jpg" class="fit image">

   여기서 baseurl이 ""로 비어있지 않다면 쌍따옴표 사이를 비우고 저장한 후 다시 빌드하면 된다. 혹은 "/blog"라고 되어 있다면 `localhost:4000/blog` 라고 주소를 입력해보면 정상적으로 볼 수 있다.



6. 터미널로 돌아가서 내 repository로 테마 파일을 푸시해준다.

   : 터미널에서 현재 위치는 *~/나의깃허브아이디.github.com* 이여야 한다. 

   ~~~
   # commit and push
   git add .
   git commit -m "Change Theme"
   git push -u origin master
   ~~~



7. 깃허브에서 commit 이 잘 되었는지 확인하고 블로그 생성을 확인한다.

   : `나의깃허브아이디.github.io` 에서 내 블로그를 볼 수 있다. 연동에는 5분 이상의 시간이 걸릴 수 있다. *(조금 기다려보자 꼭!!!!!222)





## 테마 내 것으로 만들기

블로그에 테마 설정까지 끝났다면, 세부 사항을 내 것으로 업데이트 해주어야 한다. README.md 파일을 참고하면 된다. `_config.yml` 파일에서 블로그의 타이틀 등을 변경할 수 있고, 이미지 파일 변경을 통해 프로필 사진도 등록할 수 있다!

<img src="/images/fulls/07.jpg" class="fit image">