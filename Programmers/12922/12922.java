class Solution {
    public String solution(int n) {
        String answer = "";
        for (int i = 0; i < n/2; i++) { // 2로 나는 몫의 수까지
            answer += "수박";    
        }
        if (n % 2 == 1){ // 홀수일경우 "수" 추가
            answer += "수";
        }
        return answer;
    }
}