import java.util.ArrayList;
import java.util.Arrays;

// 내가 푼 코드
class Solution {
    public int[] solution(int[] answers) {
        int[] tmp1 = {1, 2, 3, 4, 5};
        int[] tmp2 = {2, 1, 2, 3, 2, 4, 2, 5};
        int[] tmp3 = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
        int[] count = {0, 0, 0};
        for (int i = 0; i < answers.length; i++) {
            if (answers[i] == tmp1[i % tmp1.length]){
                count[0] += 1;
            } 
            if (answers[i] == tmp2[i % tmp2.length]){
                count[1] += 1;
            }
            if (answers[i] == tmp3[i % tmp3.length]){
                count[2] += 1;
            }
        }

        int maxCount = Arrays.stream(count).max().orElse(0);

        ArrayList<Integer> answerList = new ArrayList<>();
        for (int i = 0; i < count.length; i++) {
            if(count[i] == maxCount){
                answerList.add(i);
            }
        }

        int[] answer = answerList.stream().mapToInt(i -> i + 1).toArray();
        return answer;
    }
}

// // 다른 사람이 푼 코드
// class Solution {
//     public int[] solution(int[] answer) {
//         int[] a = {1, 2, 3, 4, 5};
//         int[] b = {2, 1, 2, 3, 2, 4, 2, 5};
//         int[] c = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
//         int[] score = new int[3];
//         for(int i=0; i<answer.length; i++) {
//             if(answer[i] == a[i%a.length]) {score[0]++;}
//             if(answer[i] == b[i%b.length]) {score[1]++;}
//             if(answer[i] == c[i%c.length]) {score[2]++;}
//         }
//         int maxScore = Math.max(score[0], Math.max(score[1], score[2]));
//         ArrayList<Integer> list = new ArrayList<>();
//         if(maxScore == score[0]) {list.add(1);}
//         if(maxScore == score[1]) {list.add(2);}
//         if(maxScore == score[2]) {list.add(3);}
//         return list.stream().mapToInt(i->i.intValue()).toArray();
//     }
// }
