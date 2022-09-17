import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.util.StringTokenizer;

public class Main {
    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());
        int sum, a, b;
        for (int i = 1; i <= T; i++) {
            StringTokenizer line = new StringTokenizer(br.readLine());
            a = Integer.parseInt(line.nextToken());
            b = Integer.parseInt(line.nextToken());
            sum = a + b;
            sb.append("Case #" + i + ": " + a + " + " + b + " = " + sum).append('\n');
        }

        System.out.print(sb);
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}