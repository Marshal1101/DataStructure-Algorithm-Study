import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int T, N, maxVal, val;
        String maxName, name;

        T = Integer.parseInt(br.readLine());
        for (int i = 0; i < T; i++) {
            N = Integer.parseInt(br.readLine());
            maxVal = 0;
            maxName = "";
            for (int j = 0; j < N; j++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                val = Integer.parseInt(st.nextToken());
                name = st.nextToken();
                if (val > maxVal) {
                    maxVal = val;
                    maxName = name;
                }
            }
            sb.append(maxName).append("\n");
        }

        System.out.print(sb);
    }
}