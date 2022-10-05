import java.util.Scanner;

public class Main {
    public void solution() throws Exception {
        Scanner sc = new Scanner(System.in);
        StringBuilder sb = new StringBuilder();
        int N = sc.nextInt();
        for (int i = 1; i <= N; i++) sb.append("*".repeat(i)).append('\n');
        for (int i = 1; i <= N-1; i++) sb.append("*".repeat(N-i)).append('\n');
        System.out.println(sb);
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}