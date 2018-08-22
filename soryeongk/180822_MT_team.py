import random


dataitgirls_members = '소령님,가빈님,예은님,문희님,지은k님,희영님,다현님,성윤님,소현님,새롬님,소영님,송이님,세영님,아름님,다솜님,다혜님,지윤님,예빈님,예원님,예인님,지은j님,지혜j님,진영k님,지영님,다영님,채원님,진영p님,은지님,윤경님,애란쌤,배로쌤,지현쌤,지해쌤,지혜s님,영웅님,형섭님'.split(',')
random_num_lst = [i for i in range(len(dataitgirls_members))]

member_with_num = {}
for person in dataitgirls_members:
    index = random.choice(random_num_lst)
    index = random_num_lst.pop(random_num_lst.index(index))
    member_with_num[person] = index

# print(len(dataitgirls_members))
# print(member_with_num)

'''
6명씩 6조:6으로 나눈 수가 같은거끼리(0,6,12```)
'''
n = 6
team_0 = [k for k,v in member_with_num.items() if v%n==0]
team_1 = [k for k,v in member_with_num.items() if v%n==1]
team_2 = [k for k,v in member_with_num.items() if v%n==2]
team_3 = [k for k,v in member_with_num.items() if v%n==3]
team_4 = [k for k,v in member_with_num.items() if v%n==4]
team_5 = [k for k,v in member_with_num.items() if v%n==5]

print(team_0)
print(team_1)
print(team_2)
print(team_3)
print(team_4)
print(team_5)
