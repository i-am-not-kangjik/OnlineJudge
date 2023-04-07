class Solution {
    public int[] solution(int n, int m) {
        int maxn = 0; //최대공약수
        int minn = 0; // 최소공배수

        if (m < n) {
            int tmp = n;
            n = m;
            m = tmp;
        }

        for (int i = 1; i < n+1; i++) {
            if ((m % i == 0) && (n % i == 0)) {
                maxn = i;
            }
        }

        if (m % n == 0) {
            minn = m;
        } else {
            int tmpm = m;   // m+=m으로 할경우 m의 값이 계속 커짐
            while(tmpm % n != 0){
                tmpm += m;
                if (tmpm % n == 0){
                    minn = tmpm;
                    break;
                }
            }
        }



        int[] answer = {maxn, minn};
        return answer;
    }
}