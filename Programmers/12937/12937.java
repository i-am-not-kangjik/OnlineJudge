// // 내가 한 풀이
// class Solution {
//     public String solution(int num) {
//         String answer = "Odd";
//         if (num % 2 == 0){
//             answer = "Even";
//         }
//         return answer;
//     }
// }

// 다른 사람의 풀이를 참고한 풀이

class Solution {
    public String solution(int num) {
        return (num % 2 == 0) ? "Even" : "Odd";
    }
}