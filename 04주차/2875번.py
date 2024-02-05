def max_teams(N, M, K):
    # 가능한 최대 팀 수 계산
    teams = 0
    
    # 여학생과 남학생 중 적은 수의 인원을 기준으로 팀을 구성
    while N >= 2 and M >= 1 and N + M >= K + 3:
        N -= 2
        M -= 1
        teams += 1

    return teams
# 입력 받기
N, M, K = map(int, input().split())

# 최대 팀 수 계산 및 출력
result = max_teams(N, M, K)
print(result)
