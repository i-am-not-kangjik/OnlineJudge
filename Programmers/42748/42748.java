import java.util.Arrays;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        // commands[0][0] - 1 부터 commands[0][1] - 1까지, 정렬하고 commands[0][2] -1번째 숫자
        
        for (int i = 0; i < answer.length; i++) {
            int [] tmp = Arrays.copyOfRange(array, commands[i][0] - 1, commands[i][1]); // 배열 슬라이싱
            Arrays.sort(tmp);   // 배열 정렬
            answer[i] = tmp[commands[i][2] - 1];
        }

        return answer;
    }
}