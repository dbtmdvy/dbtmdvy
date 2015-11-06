import random

a = [];

for i in range(1,10):

    a.append(i)

random.shuffle(a)

print "야구 게임 시작"

b=[0,0,0]

cnt = 1

for i in range(100):

    print "===== %2dth 시도 ====="%cnt

    cnt +=1

    x = int(raw_input("Insert 3 number : "))

    if x == 0:

        break

    for i in range(3):

        b[2-i] = x % 10

        x /= 10

    print b

    ball = 0;

    strike = 0;

    for n in range(3):

        for m in range(3):

            if a[n] == b[m] :

                if n == m:

                    strike +=1

                else :

                    ball +=1

    print "%d strike, %d ball!"%(strike,ball)

    if strike == 3:

        print "You are victory!!"

        break

print "게임 종료"
