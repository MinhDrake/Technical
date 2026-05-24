import sys

input = sys.stdin.readline

def solve():
    n = int(input())
    arr= list(map(int, input().split()))

    drops = [arr[i] - arr[i + 1] for i in range(len(arr) - 1) if arr[i] > arr[i + 1]]
    diff = max(drops) if drops else 0
    flag = 0 # 0 cong
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            if flag == 1:
                print("NO")
                return
            flag = 1
        else:
            if flag == 1 and arr[i+1] - arr[i] >= diff:
                flag = 0
    print("YES")


if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        solve()