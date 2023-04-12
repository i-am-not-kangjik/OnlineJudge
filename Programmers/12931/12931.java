// 내가 작성한 코드
// import java.util.*;

// public class Solution {
//     public int solution(int n) {
//         int answer = 0;

//        String tmp = Integer.toString(n);
//        for (int i = 0; i < tmp.length(); i++) {
//             answer +=  Character.getNumericValue(tmp.charAt(i)) ;
//        }

//         return answer;
//     }
// }

// 다른 사람의 풀이를 참고한 코드
import java.util.*;

public class Solution {
    public int solution(int n) {
        int answer = 0;

        while(true){
            answer+=n%10;
            if(n<10)
                break;

            n=n/10;
        }
        return answer;
    }
}