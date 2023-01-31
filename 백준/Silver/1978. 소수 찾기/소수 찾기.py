import sys
si=sys.stdin.readline

N = int(si())

a = list(map(int, si().split()))

answer = 0

def func(num):
    global answer
    ans = 0

    if num > 1:
        # print("num=",num)
        for i in range(1, num + 1):
            if num % i == 0:
                # print("i=",i)
                ans += 1
            if ans == 3:
                return
    
    else:
        return

    answer += 1
    return

for i in a:
    func(i)

print(answer)