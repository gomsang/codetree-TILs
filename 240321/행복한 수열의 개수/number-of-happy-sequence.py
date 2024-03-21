n, m = map(int, input().split())

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

# 행복한 수열 찾기 함수
def find_happiness(row, col):
    # 1. 각 행과 열 추출하여 리스트 생성
    # 2. 연속하는 수이면 1 추가
    # 3. 1의 개수가 (m-1) 이상이면 행복한 수열의 개수 추가하기

    num_of_happiness = 0
    rows, cols = [], []

    # 행, 열 별로 리스트에 넣기
    for i in range(row):
        h_row, h_col = [], []
        for j in range(col):
            h_row.append(grid[i][j])
            h_col.append(grid[j][i])

        rows.append(h_row) # 각 행에 대한 리스트
        cols.append(h_col) # 각 열에 대한 리스트

    # 열
    for r in rows:
        # print(r)
        cnt_same1 = []
        for a in range(len(r)-1):
            if r[a] == r[a+1]:
                cnt_same1.append(1)
            # print(cnt_same1)
        if sum(cnt_same1) >= m-1:
            num_of_happiness += 1

    for c in cols:
        # print(c)
        cnt_same2 = []
        for b in range(len(c)-1):
            if c[b] == c[b+1]:
                cnt_same2.append(1)
            # print(cnt_same2)
        if sum(cnt_same2) >= m-1:
            num_of_happiness += 1

    print(num_of_happiness)
    
find_happiness(n, n)