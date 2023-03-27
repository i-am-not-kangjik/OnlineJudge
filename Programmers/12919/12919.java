import java.util.Arrays;

class Solution {
    public String solution(String[] seoul) {
        String answer = "";
        int result = Arrays.asList(seoul).indexOf("Kim");
        answer = String.format("김서방은 %d에 있다", result);
    return answer;
    }
}