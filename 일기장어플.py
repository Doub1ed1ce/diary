#문항 리스트 목록
날씨=[
    '오늘 날씨는 어땠나요?',
    '비가 왔나요?',
    '구름이 많았나요?',
    '오늘은 따뜻했나요?',
    '날이 많이 춥진 않았나요?'
]
교통수단=[
    '걸어서 갔나요?',
    '버스를 탔나요?',
    '지하철을 탔나요?',
    '출근은 어떻게 했나요?',
    '운전을 했나요?'
]
식사메뉴=[
    '점심은 뭘 먹었나요?',
    '오늘 한식을 먹었나요?',
    '오늘 양식을 먹었나요?',
    '치킨을 먹었나요?',
    '밥은 잘 먹고 다니나요?'
]
옷=[
    '어떤 옷을 입고 갔나요?',
    '패딩은 입었나요?',
    '코트를 입었나요?',
    '포멀하게 입었나요?',
    '츄리닝을 입었나요?',
    '어떤 신발을 신었나요?'
]
랜덤질문=[
    '오늘 들은 음악은 어땠나요?',
    '오늘 몇번 웃었나요?',
    '푹 잤나요?',
    '피곤하지는 않았나요?',
]
특별한경험=[
    '좋은 사람과 함께 했나요?',
    '연인과 함께였나요?',
    '특별하게 적을만한 내용이 있나요?'
]
import random
print('일기를 써볼까요? y/n')
답변=input()
if 'y' in 답변:
    #랜덤 질문이 먼저 온다음
    랜덤선택=random.choice(랜덤질문)
    print(랜덤선택)
    랜덤선택답변=input()
    #날씨를 물어보고
    날씨선택=random.choice(날씨)
    print(날씨선택)
    날씨선택답변=input()
    #옷을 물어본다
    옷선택=random.choice(옷)
    print(옷선택)
    옷선택답변=input()
    #교통수단을 물어본다
    교통수단선택=random.choice(교통수단)
    print(교통수단선택)
    교통수단답변=input()
    #식사메뉴를 물어본다
    식사메뉴선택=random.choice(식사메뉴)
    print(식사메뉴선택)
    식사메뉴답변=input()
    #특별한 경험을 물어본다
    특별한경험선택=random.choice(특별한경험)
    print(특별한경험선택)
    특별한경험답변=input()
else:
    exit()
#저장 및 모아서 출력 기능 추가
#test