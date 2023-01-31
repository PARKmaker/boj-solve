import sys
si = sys.stdin.readline

N = int(si())
text = si().strip()
nums = []

for _ in range(N):
  nums.append(int(si()))

stack = []

for i in text:
  if "A" <= i <= "Z":
    stack.append(nums[ord(i) - ord("A")])

  else:
    num2 = stack.pop()
    num1 = stack.pop()
    
    if i == "+":
      stack.append(num1+num2)
    elif i == "-":
      stack.append(num1-num2)
    elif i == "*":
      stack.append(num1*num2)
    elif i == "/":
      stack.append(num1/num2)

  # print(stack)

print("%.2f" %stack[0])