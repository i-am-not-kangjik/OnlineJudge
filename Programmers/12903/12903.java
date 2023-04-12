// 내 풀이
// class Solution {
//     public String solution(String s) {
//         String answer = "";
//         if (s.length() % 2 == 1){
//             answer += s.charAt(s.length() / 2);
//         }
//         else {
//             answer += s.charAt(s.length() / 2 - 1);
//             answer += s.charAt(s.length() / 2);
//         }
//         return answer;
//     }
// }

// 다른 사람의 풀이를 참고한 풀이
class Solution {
    public String solution(String s) {
        return s.substring((s.length() - 1) / 2, s.length() / 2 + 1);
    }
}