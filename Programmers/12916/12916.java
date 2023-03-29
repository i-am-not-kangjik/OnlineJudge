import java.util.Arrays;
import java.util.Collections;

class Solution {
    boolean solution(String s) {
        boolean answer = true;
        s = s.toLowerCase();
        // s의 전체 길이에서 p,y를 공백으로 대체한 문장의 길이를 빼면 p,y의 개수 파악 가능
        int pcnt = s.length() - s.replaceAll("p", "").length();
        int ycnt = s.length() - s.replaceAll("y", "").length();
        if (pcnt != ycnt){
            answer = false;
        }
        return answer;
    }
}