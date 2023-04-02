import java.util.Scanner;

class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();

        for (int i = 0; i < b; i++) {   // 세로줄이 바깥 for문
            for (int j = 0; j < a; j++) {
                System.out.print('*');
            }
            if (i != b-1){
                System.out.println();
            }
        }
    }
}