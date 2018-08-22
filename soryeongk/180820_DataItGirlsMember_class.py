import random

class DataItGirls:
    def __init__(self, _name):
        self._name = _name
        self.where = 0

    def say_something(self, _freq_saying=None):
        if _freq_saying != None:
            self._freq_saying = _freq_saying
            return self._name + ' : ' + self._freq_saying
        else:
            return self._name + ' : 쥬금 x_x'

    def dice(self):
        self.where += random.randint(1,6)
        return self.where

print('\n')
soryeong = DataItGirls('soryeong')

board = {}
for i in range(1,31):
    board[i] = random.choice(['맥주', '소주', '와인', '사케']) + random.choice(['한 방울', '한 모금', '두 모금', '한 잔', '두 잔'])

for _ in range(5):
    board[random.randint(6,30)] = 'backward'
# print(board)

soryeong.dice()
where = soryeong.where

if board[where] == 'backward':
    where -= random.randint(1,5)
print('{} : 현재 위치는 {}입니다.'.format(soryeong._name, where))
print('벌칙은 {}입니다.'.format(board[where]))

# print(soryeong.say_something())
#
# print('\n')
# jinkim = DataItGirls('JinKim')
# print(jinkim.say_something(_freq_saying='갈아 넣어요 우리'))
#
# print('\n')
# seyomi = DataItGirls('seyomi')
# print(seyomi.say_something(_freq_saying='헐 ㄷㅂ'))
#
# print('\n')
# alan = DataItGirls('Alan')
# print(alan.say_something(_freq_saying='(꾸벅) 안녕하세요 :-)'))
#
