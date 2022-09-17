import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {
    public int GCD(int a, int b) throws Exception {
        int tmp;
        while (b > 0) {
            tmp = a % b;
            a = b;
            b = tmp;
        }
        return a;
    }

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        int N;
        long totalGCD;
        int[] arr = new int[101];
        int T = Integer.parseInt(br.readLine());
        for (int i = 0; i < T; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            totalGCD = 0;
            N = Integer.parseInt(st.nextToken());
            for (int j = 0; j < N; j++) {
                arr[j] = Integer.parseInt(st.nextToken());
                for (int k = 0; k < j; k++) {
                    totalGCD += this.GCD(arr[k], arr[j]);
                }
            }

            sb.append(totalGCD).append('\n');
        }

        bw.write(sb.toString());
        bw.flush();
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}