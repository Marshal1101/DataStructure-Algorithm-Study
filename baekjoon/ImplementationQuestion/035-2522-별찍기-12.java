import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        StringBuilder sb = new StringBuilder();
        int N = sc.nextInt();

        for (int i = N-1; i > 0; i--) {
            sb.append(" ".repeat(i)).append("*".repeat(N-i)).append('\n');
        }
        for (int i = 0; i < N; i++) {
            sb.append(" ".repeat(i)).append("*".repeat(N-i)).append('\n');
        }

        System.out.println(sb);
    }
}