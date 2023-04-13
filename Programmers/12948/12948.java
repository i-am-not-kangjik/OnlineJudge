// 내 풀이
// class Solution {
//     public String solution(String phone_number) {
//         String tmp = phone_number.substring(0, phone_number.length()-4)
//         .replaceAll("[0-9]", "*");
        
//         String answer = tmp + phone_number.substring(phone_number.length()-4);

//         return answer;
//     }
// }

// 다른 사람의 풀이를 참고한 풀이
class Solution{
    public String solution(String phone_number) {
        char[] ch = phone_number.toCharArray();
        for (int i = 0; i < ch.length - 4; i++) {
            ch[i] = '*';
        }
        return String.valueOf(ch);
    }
}