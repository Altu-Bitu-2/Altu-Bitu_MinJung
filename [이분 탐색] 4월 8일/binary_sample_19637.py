# 백준 19637
# IF문 좀 대신 써줘
# 샘플 코드에 주석 달아 추가제출 --> 나중에 다시 풀어보기

import sys
from bisect import bisect_left
input = sys.stdin.readline

"""
 [IF문 좀 대신 써줘]
 모든 캐릭터와 칭호를 매칭하는 브루트 포스를 사용하기엔 최대 연산 횟수 10^5 * 10^5 -> 100억!
 특정 전투력 '이하'까지 해당하는 칭호를 받을 수 있음
 -> 이분 탐색
"""

# 입력
n, m = map(int, input().split()) # 칭호의 개수, 칭호를 출력해야 하는 캐릭터들의 개수 입력
names = [] # 칭호 리스트
power = [] # 전투력 리스트

# 이미 능력치에 대한 오름차순으로 입력되므로 정렬 필요 X
for _ in range(n):
    name, p = input().split() # 칭호와 전투력 입력
    names.append(name) # 칭호 리스트에 추가
    power.append(int(p)) # 전투력 리스트에 추가

# bisect_left(array, value): array에 value를 삽입할 수 있는 가장 왼쪽 인덱스를 리턴함
# 따라서 리턴 받은 인덱스로 name을 조회하면 가장 먼저 받은 칭호가 된다!
for _ in range(m):
    print(names[bisect_left(power, int(input()))])