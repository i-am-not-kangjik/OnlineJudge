// 내 풀이
class Solution {
    public boolean solution(int x) {
        int tmp = 0;
        int originX = x;
        while (x != 0) {
            tmp += x % 10;
            x /= 10;
        }
        return originX % tmp == 0 ? true : false;
    }
}

// // 다른 사람의 풀이
// class Solution {
//     public boolean solution(int x) {
//         String [] tmp = String.valueOf(x).split("");
//         int sum=0;
//         for(String s:tmp) {
//             sum+=Integer.parseInt(s);
//         }
//         return x % sum == 0;
//     }
// }