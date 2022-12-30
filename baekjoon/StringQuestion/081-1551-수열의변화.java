import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine(), ",");
        int[] ret = new int[N];
        for (int i = 0; i < N; i++) {
            ret[i] = Integer.parseInt(st.nextToken());
        }

        int k = 0;
        while (k++ < K) {
            for (int i = 0; i < N-k; i++) {
                ret[i] = ret[i+1] - ret[i];
            }
        }

        StringBuilder sb = new StringBuilder();
        sb.append(ret[0]);
        for (int i = 1; i < N-K; i++) {
            sb.append(","+ String.valueOf(ret[i]));
        }

        System.out.println(sb.toString());
    }
}