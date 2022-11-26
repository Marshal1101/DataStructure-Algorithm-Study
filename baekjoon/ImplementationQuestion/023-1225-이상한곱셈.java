import java.util.StringTokenizer;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        String A = sc.next();
        String B = sc.next();
        int a, b;
        long total = 0;
        for (int i = 0; i < A.length(); i++) {
            a = A.charAt(i) - '0';
            for (int j = 0; j < B.length(); j++) {
                b = B.charAt(j) - '0';
                total += a * b;
            }
        }
        System.out.print(total);
    }
}