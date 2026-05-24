import sys

input = sys.stdin.readline

def solve():
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        ans = ( max(a) - min(a) + 1)// 2
        print(ans)


if __name__ == "__main__":
    solve()