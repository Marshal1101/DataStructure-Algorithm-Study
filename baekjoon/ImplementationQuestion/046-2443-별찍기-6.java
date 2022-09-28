import java.util.Scanner;

public class Main {
    public void solution() throws Exception {
        Scanner sc = new Scanner(System.in);
        StringBuilder sb = new StringBuilder();

        int N = sc.nextInt();
        int T = 2 * N - 1;

        for (int i = 0; i < N; i++) {
            sb.append(" ".repeat(i)).append("*".repeat(T-2*i)).append('\n');
        }

        System.out.println(sb);
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}