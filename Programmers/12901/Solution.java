// // 내가 푼 코드
// class Solution {
//     public String solution(int a, int b) {
//         String[] day = new String[] {"SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"};

//         int startDay;
//         if (a == 5){
//             startDay = 0;
//         } else if (a == 2 || a == 8) {
//             startDay = 1;
//         } else if (a == 3 || a == 11) {
//             startDay = 2;
//         } else if (a == 6) {
//             startDay = 3;
//         } else if (a == 9 || a == 12) {
//             startDay = 4;
//         } else if (a == 1 || a == 4 || a == 7) {
//             startDay = 5;
//         } else {
//             startDay = 6;
//         }

//         String answer = day[(startDay + b - 1) % 7];
//         return answer;
//     }
// }

// 다른사람의 풀이를 참고한 코드
class Solution {
    public String solution(int a, int b) {
        String answer = "";
  
        int[] dayMonth = {31,29,31,30,31,30,31,31,30,31,30,31};
        String[] day ={"FRI","SAT","SUN","MON","TUE","WED","THU"};
        int startDate = 0;
        for(int i = 0 ; i< a-1; i++){
            startDate += dayMonth[i];
        }
        startDate += b-1;
        answer = day[startDate %7];
  
        return answer;
    }
  }
  