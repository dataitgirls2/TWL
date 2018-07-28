### 20180709_github blog
***
- github으로 블로그 만들기 

  1. 깃헙 아이디.github.com 로 새 레파지토리 만들기

  2. github pages - source -  (gh-pages-branch) 

  3. setting - github pages - choose a theme

  4. 마크다운 파일 생성, 블로그 글 작성

     

- ruby, jekyll 설치 및 사용

1. **https://rubyinstaller.org/downloads/**  다운

2. gem install jekyll

3. cd c://내 깃헙 이름/깃허브사용자명.github.com

4. jekyll new.  //위 경로에 지킬 생성

5. jekyll serve --watch //서버구동, 구동 멈출 때는 ctrl-c

6. 버전관리 

   ```
   git add
   git commit -m "initialize blog"
   git push origin master
   ```

7.  _config.yml파일을 열어 수정  //소스트리에서 jekyll설정

8.  수정 후 jekyll serve --watch로 서버 재시작. 

9.  gem install bundler 번들러 설치 후 jekyll theme 설정
