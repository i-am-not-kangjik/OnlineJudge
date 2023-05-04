class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        int[] students = new int[n];
        
        for (int i = 0; i < students.length; i++) {
            students[i] = 1;
        }

        for (int i = 0; i < lost.length; i++) {
            students[lost[i] - 1]--;
        }

        for (int i = 0; i < reserve.length; i++) {
            students[reserve[i] - 1]++;
        }
        for (int i = 0; i < students.length; i++) {
            if (students[i] == 0) {
                if (i > 0 && students[i - 1] == 2){
                    students[i] = 1;
                    students[i-1]--;
                }
                else if (i < n - 1 && students[i + 1] == 2) {
                    students[i] = 1;
                    students[i + 1]--;
                }
            }
        }

        int answer = 0;

        for (int i = 0; i < students.length; i++) {
            if (students[i] != 0) {
                answer += 1;
            }
        }
        
        return answer;
    }
}