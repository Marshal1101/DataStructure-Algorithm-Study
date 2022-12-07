import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int N, diff;
        String X, Y;
        N = Integer.parseInt(br.readLine());
        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            sb.append("Distances:");
            X = st.nextToken();
            Y = st.nextToken();
            for (int j = 0; j < X.length(); j++) {
                diff = Y.charAt(j) - X.charAt(j);
                if (diff < 0) diff += 26;
                sb.append(" " + diff);
            }
            sb.append("\n");
        }
        System.out.print(sb);
    }
}