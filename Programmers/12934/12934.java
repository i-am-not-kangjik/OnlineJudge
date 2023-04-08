class Solution {
    public long solution(long n) {
        long answer = (long) Math.sqrt(n);
        if ((int) answer * (int) answer == (int) n) {
            answer = (answer + 1) * (answer + 1);
        } else answer = -1;
        return answer;
    }
}