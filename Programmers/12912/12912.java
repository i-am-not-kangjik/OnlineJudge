// 내 풀이
// class Solution {
//     public long solution(int a, int b) {
//         long answer = 0;
//         if (a == b){
//             return a;
//         }
//         else if (b < a){ // a가 더 큰 경우 스왑
//             int tmp;
//             tmp = a;
//             a = b;
//             b = tmp;
//         }
//         for (int i = a; i < b+1; i++){
//             answer += i;
//         }
//         return answer;
//     }
// }

// 다른 사람의 풀이를 참고한 풀이
class Solution {
    public long solution(int a, int b) {
        if (a == b){
            return a;
        }
        
        long answer = 0;
        int start = Math.min(a, b);
        int end = Math.max(a, b);

        for (int i = start; i < end+1; i++){
            answer += i;
        }
        return answer;
    }
}