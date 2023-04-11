import java.util.*;


public class Solution {
    public int[] solution(int []arr) {
        ArrayList<Integer> tmp = new ArrayList<>();
        tmp.add(arr[0]);
        int tmpCnt = 0;     // arraylist의 원소와 비교할 인덱스
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] != tmp.get(tmpCnt)){
                tmp.add(arr[i]);
                tmpCnt += 1;
            }
        }
        //ArrayList를 int 배열로 변한
        int[] answer = new int[tmp.size()];
        for (int i = 0; i < tmp.size(); i++) {
            answer[i] = tmp.get(i);
        }
        return answer;
    }
}