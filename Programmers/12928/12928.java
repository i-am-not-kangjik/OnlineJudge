// // 내가 한 풀이 0.05, 75MB
// class Solution {
//     public int solution(int n) {
//         int answer = 0;
//         for (int i = 1; i < n + 1; i++) {
//             if (n % i == 0){
//                 answer += i;
//             }
//         }
//         return answer;
//     }
// }

// 다른 사람의 풀이 참고 0.05, 75MB (비슷함)
class Solution {
    public int solution(int n) {
        int answer = 0;
        for (int i = 1; i < n / 2 + 1; i++) {
            if (n % i == 0){
                answer += i;
            }
        }
        answer += n;
        return answer;
    }
}