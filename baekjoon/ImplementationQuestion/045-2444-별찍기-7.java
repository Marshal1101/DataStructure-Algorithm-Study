import java.util.Scanner;

public class Main {
    public void solution() throws Exception {
        Scanner sc = new Scanner(System.in);
        StringBuilder sb = new StringBuilder();
        int N = sc.nextInt();

        for (int i = 1; i <= N; i++) {
            sb.append(" ".repeat(N-i)).append("*".repeat(2*i-1)).append('\n');
        }
        for (int i = 1; i < N; i++) {
            sb.append(" ".repeat(i)).append("*".repeat(2*(N-i)-1)).append('\n');
        }

        System.out.println(sb);
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}