class Solution {
    public long solution(int a, int b) {
        long answer = 0;
        if (a == b){
            return a;
        }
        else if (b < a){
            int tmp;
            tmp = a;
            a = b;
            b = tmp;
        }
        for (int i = a; i < b+1; i++){
            answer += i;
        }
        return answer;
    }
}