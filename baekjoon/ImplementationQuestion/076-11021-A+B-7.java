import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.util.StringTokenizer;

public class Main {
    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());
        int sum = 0;
        for (int i = 1; i <= T; i++) {
            StringTokenizer line = new StringTokenizer(br.readLine());
            sum = Integer.parseInt(line.nextToken()) + Integer.parseInt(line.nextToken());
            sb.append("Case #" + i + ": " + sum).append('\n');
        }

        System.out.print(sb);
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}