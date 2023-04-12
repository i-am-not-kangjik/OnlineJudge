// 내가 푼 코드
// class Solution {
//     public boolean solution(String s) {
//         boolean answer = true;
//         if (s.length() != 4 && s.length() != 6){
//             answer = false;
//             return answer;
//         }
//         for (int i = 0; i < s.length(); i++) {
//             if (s.charAt(i) < 48 || s.charAt(i) > 57){
//                 answer = false;
//                 return answer;
//             }
//         }
//         return answer;
//     }
// }

// 다른 사람이 푼 코드
class Solution {
    public boolean solution(String s) {
      return (s.length() != 4 && s.length() != 6) || (s.split("[0-9]").length > 0) ? false:true;
    }
  }
  