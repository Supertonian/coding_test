// https://school.programmers.co.kr/learn/courses/30/lessons/147355
#include <string>

using namespace std;

bool compare_string(string a, string b, int length) {
    // a가 b보다 같거나 크면 true
    for (int i=0; i < length; i++) {
        if (a[i] > b[i]) {
            return true;
        } else if (a[i] < b[i]) {
            return false;
        }
    }
    return true;
}

int solution(string t, string p) {
    int t_length = t.length();
    int p_length = p.length();
    
    int answer = 0;
    
    for (int i = 0; i < t_length - p_length + 1; i++) {
        string substring = t.substr(i, p_length);
        if (compare_string(p, substring, p_length)) {
            answer += 1;
        }
    }
    return answer;
}
