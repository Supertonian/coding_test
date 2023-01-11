# https://school.programmers.co.kr/learn/courses/30/lessons/150370

def diff_in_months(a: str, b: str) -> int:
    (a_y, a_m, a_d) = a.split('.') # 오늘
    (b_y, b_m, b_d) = b.split('.') # 비교 날짜
    
    year_diff = (int(a_y) - int(b_y)) * 12
    month_diff = (int(a_m) - int(b_m))
    
    # 날짜가 더 앞서가는것은 상관없으나 더 작다면 월 -1
    day_diff = 0 if (int(a_d) - int(b_d)) > -1 else -1
    
    return year_diff + month_diff + day_diff

def solution(today, terms, privacies):
    answer = []
    
    # terms into dictionary
    term = {}
    for t in terms:
        (k, v) = t.split(' ')
        term[k] = v
    
    # find expired date
    for index, privacy in enumerate(privacies):
        (_date, _type) = privacy.split(' ')
        
        if not diff_in_months(today, _date) < int(term[_type]):
            answer.append(index + 1)
        
    return answer
