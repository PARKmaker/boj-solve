import sys
si = sys.stdin.readline

text = si().strip()
answer = []
sign = []

def operFunc(oper):
  if oper == "*" or oper == "/":
    return True

for i in text:

  if "A" <= i <= "Z":
    answer.append(i)

  else:
    if i == "(":
      sign.append(i)
    
    elif operFunc(i):
      while sign and (operFunc(sign[-1])):
        answer.append(sign.pop())
      sign.append(i)

    elif i == '+' or i == '-':
      while sign and sign[-1] != "(":
        answer.append(sign.pop())
      sign.append(i)
    
    elif i == ")":
      while sign and sign[-1] != "(":
        answer.append(sign.pop())
      sign.pop()

while sign:
  answer.append(sign.pop())

print("".join(answer))
