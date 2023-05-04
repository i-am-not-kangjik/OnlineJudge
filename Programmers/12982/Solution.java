import java.util.Arrays;

// 내가 한 풀이
class Solution {
    public int solution(int[] d, int budget) {
        int answer = 0;
        int count = 0;
        Arrays.sort(d);
        for (int i = 0; i < d.length; i++) {
            if (count + d[i] <= budget){
                count += d[i];
                answer += 1;
            } else break;
        }
        return answer;
    }
}

// 다른 사람의 풀이
// import java.util.*;

// class Solution {
//   public int solution(int[] d, int budget) {
//       int answer = 0;

//         Arrays.sort(d);

//         for (int i = 0; i < d.length; i++) {
//             budget -= d[i];

//             if (budget < 0) break;

//             answer++;
//         }

//         return answer;
//   }
// }
