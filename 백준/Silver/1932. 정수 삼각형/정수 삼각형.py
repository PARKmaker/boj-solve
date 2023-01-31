import sys
si = sys.stdin.readline

def main():
  n = int(si())

  a = []
  dp = [[0 for _ in range(501)] for i in range(501)]

  for i in range(1, n+1):
    a = [0]+list(map(int,si().split()))

    for j in range(1, len(a)):
      dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + a[j]

  print(max(dp[n]))

if __name__ == "__main__":
    main()