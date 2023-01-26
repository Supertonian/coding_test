# https://school.programmers.co.kr/learn/courses/30/lessons/147354
#
# 문제에 주어진 1~4번 스텝 정확하게 따라하니 바로 풀렸음.
#

from array import array

def solution(data, col, row_begin, row_end):
    # ** 문제의 정렬기준에 맞게 정렬 **
    # 테이블의 튜플을 col번째 컬럼의 값을 기준으로 오름차순 정렬을 하되,
    # 만약 그 값이 동일하면 기본키인 첫 번째 컬럼의 값을 기준으로 내림차순 정렬합니다.
    data.sort(key=lambda x : (x[col-1], -x[0]))
    
    # S_i를 i 번째 행의 튜플에 대해 각 컬럼의 값을 i 로 나눈 나머지들의 합으로 정의합니다.
    # row_begin ≤ i ≤ row_end 인 모든 S_i를 누적하여
    # unsigned int
    s_list = array('I')
    while row_begin <= row_end:
        S = 0
        for d in data[row_begin-1]:
            S += (d % row_begin)
        s_list.append(S)
        row_begin += 1
        
    # bitwise XOR 한 값을 해시 값으로서 반환합니다.
    answer = s_list.pop(0)
    for i in range(len(s_list)):
        answer ^= s_list[i]

    return answer
