package baekjoon;
import java.util.*;

// 클래스 명만 바꿔서 Main 클래스에 복붙
public class level3_11021 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int T = sc.nextInt();
        int[] box = new int[T];
        int a;
        int b;

        for (int i = 0; i < T; i++) {
            a = sc.nextInt();
            b = sc.nextInt();
            box[i] = a + b;
        }

        for (int i = 1; i <= T; i++) {
            System.out.println("Case #" + i + ": " + box[i - 1]);
        }

    }
}