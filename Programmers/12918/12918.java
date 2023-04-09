class Solution {
    public boolean solution(String s) {
        boolean answer = true;
        if (s.length() != 4 && s.length() != 6){
            answer = false;
            return answer;
        }
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) < 48 || s.charAt(i) > 57){
                answer = false;
                return answer;
            }
        }
        return answer;
    }
}