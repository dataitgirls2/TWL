# Blog 생성하기

### 1. Github에서 repository생성하기

- repository의 이름은 (내계정).github.com
- MIT license, README file 생성
- 생성 후 settings - Github pages 하단 Theme설정



### 2. local에 clone 및 Jekyll 설치

- C드라이브에서 gitbash 실행 후

```
git clone (clone할 새 repository git주소)
```



- Jekyll 설치

```
gem install jekyll
```



- clone된 폴더로 이동하여 Jekyll 생성

```
jekyll new .
```



### 3. server 구동 및 commit

- commit 전 local에서 확인하기

```
jekyll serve --watch
```



- local주소로 들어가 확인하기
- 확인한 사항을 github에 반영

```
git add .

git commit -m "commit message"

git push origin master
```



### 4. Jekyll  설정하기

- local의 clone 폴더 내 _config.yml 파일 수정

  atom편집기를 열어 title 및 username을 수정하여 저장

- server 구동하여 변경사항을 확인하기

- 반영한 사항을 다시 commit하여 github에 반영하기

```
git add .

git commit -m "commit message"

git push origin master
```



### 5. 새 Post 업로드하기

- Typora file을 작성한 후 파일명 형식에 맞게 2018-07-09-How-to-install-jekyll로 저장
- local의 _posts 폴더에 추가
- server 구동하여 확인
- github에 push하기
