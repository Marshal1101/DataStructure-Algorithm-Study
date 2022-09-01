import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.util.StringTokenizer;

public class Main {
    public void permentation(int order, int N, int M, boolean[] visited, int[] ans, StringBuilder sb) throws Exception {
        for (int i = 1; i <= N; i++) {
            if (!visited[i]) {
                visited[i] = true;
                ans[order] = i;
                if (order == M) {
                    String num;
                    for (int k = 1; k <= M; k++) {
                        num = String.valueOf(ans[k]);
                        sb.append(num).append(' ');
                    }
                    sb.append('\n');
                } else {
                    this.permentation(order+1, N, M, visited, ans, sb);
                }
                visited[i] = false;
            }
        }
    }

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[] ans = new int[M+1];
        boolean[] visited = new boolean[N+1];
        this.permentation(1, N, M, visited, ans, sb);

        System.out.println(sb);
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}