# 180807

## HTTP API 활용하기 + 테스트 주도 개발

### 오전수업 애란쌤

#### Git 과 Github을 뽀개보자

- Seyoungbot 프로젝트 만들기
- `MIT라이센스` : 하고싶은대로 다 하세요
- `GPL라이센스` : 무조건 gpl이 되어야 함.
- 라이센스가 명시되어있지 않다면, 원 저작권자에게 물어보아야 함.



- `create a new project` 를 누르는 순간 깃헙 서버에 내 레파지토리가 생김.
- clone을 해오면 copy해서 완전히 똑같음.
- `ㅣㅣ` 리스트 보여짐
- `-v` verbal "장황하게 말해봐" 라는 의미
- git 을 클론해오면 원래 저장소에 origin이라는 이름을 붙여 줌.



![1533608240193](C:\Users\wolever\AppData\Local\Temp\1533608240193.png)

- `git status`아톰에서 만든 새로 만든 파일은 tracking 되지 않는다고 나옴. 
- `git add ma[tab]` : tab누르면 그거로 시작하는 이름의 파일 바로 찾아서 입력됨. (`git add main.py` 찾아졌음)



다음으로, main.py파일을 변경한 다음, 아래의 내용을 수행해보기

```bash
wolever@wolever-PC MINGW64 /d/projects/seyoungbot (master)
$ git status
On branch master
Your branch is up to date with 'origin/master'.

Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

        new file:   main.py

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

        modified:   main.py

wolever@wolever-PC MINGW64 /d/projects/seyoungbot (master)
$ git checkout -- main.py
```

- `git checkout -- main.py`하면 이전 버전으로 돌아갈 수 있음.

- `git commit -m "Hello world 작성"`

- $ git status
  On branch master
  Your branch is ahead of 'origin/master' by 1 commit.
    (use "git push" to publish your local commits)

  nothing to commit, working tree clean

  커밋할 게 없고 파일이 같은 상태

- `pwd` Print Working Directory



아나콘다 프롬프트를 실행한 다음, change directory를 projects 폴더로 변경한 후`python main.py` 를 실행해보면 "Hello World! " 가 실행됨.

- `python` 실행해보면 3.6.x 버전확인, `quit()` 실행해서 빠져나옴.



`git push` : 레퍼지토리 생성 시 master가 default로 생김. origin의 master로 기본으로 push됨.

`fork` 깃헙에서 편의상 만든 용어. 깃헙 상에서 내 옆사람의 레퍼지토리를 나의 공간으로 clone해 온 것.

- download / upload 의 멘탈모델처럼, upstream이 본래의 레포지토리가 됨.



`git diff` : 수정된 내용 보여짐.



- 태초에 파일이 있었다. > 수정 > untracked > add > tracked & staged > 수정 > tracked & modified > add > tracked & staged > commit > committed
- 오늘 하루종일 작업을 하다가 망친경우, `git diff`로 변경을 확인해보고, 
- `git status`로 쓸수 있는 것을 확인해봄,
- `git checkout -- main.py` 로 오늘 하루종일 수정했던 내용을 싹 지워버리기 가능. (커밋된 파일들은 거의 다 기록이 남지만, add된 상태는)



풀리퀘를 보냈는데 컨플릭이 나면 보통 풀리퀘를 보낸 사람이 컨플릭을 해결해야 함. (merge해주는 원 주인이 클릭 한번에 merge하기 편하기 때문)

- `git add upstream 주소` 로 upstream을 설정해줌.

- `git fetch upstream` git ignore 파일 어딘가에 upstream의 바뀐 내용을 저장해 둠 (upstream의 실제 커밋을 내 컴퓨터로 가져오는 것). 하지만 working directory에 반영되는 것은 아님.
- `git merge upstream/master` 변경된 내용들을 merge 해 줌. 현재 브랜치와 fetch에서 받아온 것을 합쳐라. 라는 것.
- 다음 아톰창을 키면, 내것과 상대방의 코딩이 동시에 있음.
- 그리고 git status 확인해 보고 add해줌

`rebase`는 위의 과정들을 깔끔히 해주는 굉장히 강력한 도구. 하지만 잘 사용해야 함.



## Create a new repository - 봇 만들기 실습

#### 개발환경 만들기

`pip install pipenv` 파이썬 개발 환경을 만들어주는 패키지를 설치. 프로젝트별 환경을 격리시켜 줌. 각각의 프로젝트간 충돌이 나기도 하는데, pipenv로 각 프로젝트 환경을 격리시켜줌. (해당 프로젝트의 디렉토리에서 해줌)

`pipenv --python=3.6` 로 환경을 맞춰 줌. 해당 폴더 가보면 Pipfile이란 파일이 하나 생긴것을 확인할 수 있음.



#### 슬랙봇의 뼈대 만들기

https://api.slack.com 로 이동하기

Bot Users > Create > Install Alpp 눌러서 봇 만들고, 추가해주기.

`pipenv install rtmbot` 으로 깔아주기(real time bot이라고 이미 누군가가 만들어 놓은 실시간 봇)

```python
from rtmbot import RtmBot

config = {
    "SLACK_TOKEN": "xoxb-...",
    "ACTIVE_PLUGINS": []
}
# 봇이 작동하기 위한 코딩들이 딕셔너리 형태로 들어있음. 봇이 내부에서 정보를 연결해서 슬랙에 연결됨.

bot = RtmBot(config)
bot.start()
```

- slack_token 을 넣어주어야 함.
- api.slack.com 에 접속 > 우상단 your apps > Install App에 Bot User OAuth Acceess Token 을 적어줌.
- 봇 실행시키기 : `pipenv run python main.py` 
- 봇 끄기: `crtl + c`

봇 실행시키면, 시간, 유저이름, 채널의 고유 번호, 내용 등이 딕셔너리의 형태로 담김.

```python
class HelloPlugin(Plugin):
    def process_message(self, data):
        if "애란" in data["text"]:
        self.outputs.append([data["channel"], "불렀어?"])
```

Pipfile과 Pipfile.lock는 버전관리를 해주어야 다른 개발자들이 사용할 때에도 내 프로젝트와 똑같은 환경으로 해줄 수 있기 때문에 함께 올려주어야 함.



### 테스트 주도 개발

봇을 만들다보면 충돌이 일어날 수 있음. 만약 위와 아래에서 같은 text(가정법의 '라면', 음식 '라면')를 잡아내는 프로그램을 짜는 경우 밑의 코딩은 한번도 실행되지 않을 수 있음. 하지만 이런 종류의 버그는 당장 에러가 발생하지 않은 채 프로그램이 진행됨. 그런 버그가 점점 쌓여가며 프로젝트가 망해감.

하지만 모든 코딩을 수정할 때 마다 slack을 껐다 켰다 하기도 힘듬.

```python
def reply(text):
	if "애란" in text:
		return "불렀어?"
	elif "주사위" == text:
		die = sstr(random.randint(1,6))
		return "주사위를 던졌더니" + die + "나왔다."
	else:
		return None

class HelloPlugin(Plugin):
    def process_message(self, data):
        answer = reply(data["text"])
        if answer is None:
        	pass
        elif:
         self.outputs.append([data["channel"], answer])
```

