# https://school.programmers.co.kr/learn/courses/30/lessons/148653
#
# 자료구조보다 패턴을 이용해서 풀려고 했음.
# 5보다 크면 -10을 하는게 -1하는것보다 0을 더 빨리간다는 것을 찾아서 풀었음.
#
# 예) 6이면 -1 6번 하는것보다 -10한번 +1 4번으로 0에 도달하는것이 더 빠르다.
# 예) 4면 -1 4번해서 0도착하는것이 가장 빠르다.
#
# 반복문으로 값이 0이 될때까지 돌리고 0이 되면 시도한 횟수 answer return한다.
#
# 1부터 100을 돌리면 대부분 통과하지만 실패하는 케이스들이 발생한다.
# 그 예외 케이스를 분석하니 두자릿수 이상이 되면 앞에 두개가 5보다 같거나 크면 -10x를 해주는것이 0에 더 빨리 도달한다.
#
# 예) 56이면 기존로직이면 -10을 6번하고 +1을 4번해서 총 10번만에 도착하는데
# 더 빠른 방법은 -100을 1번, +10을 4번 +1을 4번으로 총 9번만에 도착 가능하다.
# 55도 동일하고 59도 동일하다. 60부터는 앞자리가 6이기 때문에 처음부터 -100을 시도함.
#

def check_first_two(items: str):
    if len(items) < 2:
        return False
    
    return items[0] >= '5' and items[1] >= '5'

def solution(storey):
    answer = 0

    while storey != 0:
        abs_in_str = str(abs(storey))
        first_number = int(abs_in_str[0])
        length = len(abs_in_str) - 1
        add = 0
        is_positive = storey > 0
        
        if first_number > 5 or check_first_two(abs_in_str):
            # less than 0 -> +10xx
            # greater than 0 -> -10xx
            add = (-1 if is_positive else 1) * (10 ** (length+1))
        else:
            # less than 0 -> +1xx
            # greater than 0 -> +1xx
            add = (-1 if is_positive else 1) * (10 ** length)

        storey += add
        answer += 1
    return answer



