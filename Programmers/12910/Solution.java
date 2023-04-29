import java.util.ArrayList;
import java.util.Arrays;


// // 내가 푼 코드
// class Solution {
//     public int[] solution(int[] arr, int divisor) {
//         Arrays.sort(arr);
//         ArrayList<Integer> tmp = new ArrayList<>();
//         for (int integer : arr) {
//             if (integer % divisor == 0) {
//                 tmp.add(integer);
//             }
//         }
//         if (tmp.size() == 0) {
//             return new int[]{-1};
//         } 
//         int[] answer = tmp.stream().mapToInt(Integer::intValue).toArray();
//         return answer;
//     }
// }

// 다른 사람의 풀이를 참고한 코드
class Solution {
    public int[] solution(int[] arr, int divisor) {
        int[] answer = Arrays.stream(arr).filter(i -> i % divisor == 0).sorted().toArray();
        return answer.length == 0? new int[]{-1} : answer;
    }
}