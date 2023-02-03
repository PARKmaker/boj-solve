def gcd(a, b):
    while b:
        r = a % b
        a = b
        b = r
    return a

def solution(arr):
    answer = 1
    
    for i in arr:
        answer = (answer * i) // gcd(answer, i)
    
    print(answer)
    return answer