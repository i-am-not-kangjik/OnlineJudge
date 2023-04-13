// 내 풀이
// class Solution {
//     public int[] solution(long n) {
//         int len = String.valueOf(n).length(); // n의 길이 구하기
//         int[] answer = new int[len];

//         for (int i = 0; i < answer.length; i++) {
//             answer[i] = (int) (n % 10);   
//             n /= 10; 
//         }

//         return answer;
//     }
// }

// 다른 사람의 풀이를 참고한 코드
class Solution {
    public int[] solution(long n) {
        String s = String.valueOf(n);
        StringBuilder sb = new StringBuilder(s);
        sb = sb.reverse();
        String[] ss = sb.toString().split("");
  
        int[] answer = new int[ss.length];
        for (int i=0; i<ss.length; i++) {
            answer[i] = Integer.parseInt(ss[i]);
        }
        return answer;
    }
  }