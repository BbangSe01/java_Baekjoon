package baekjoon;

import java.util.*;

// 클래스명만 Main으로 바꿔서 복붙
public class level3_2438 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();

        for (int i=1;i<=N;i++){
            for(int j=0;j<i;j++){
                System.out.print("*");
            }
            System.out.println("");
        }
    }
}
