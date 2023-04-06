import java.util.*;

public class Solution {
    public int solution(int n) {
        int answer = 0;

       String tmp = Integer.toString(n);
       for (int i = 0; i < tmp.length(); i++) {
            answer +=  Character.getNumericValue(tmp.charAt(i)) ;
       }

        return answer;
    }
}