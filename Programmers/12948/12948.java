class Solution {
    public String solution(String phone_number) {
        String tmp = phone_number.substring(0, phone_number.length()-4)
        .replaceAll("[0-9]", "*");
        
        String answer = tmp + phone_number.substring(phone_number.length()-4);

        return answer;
    }
}