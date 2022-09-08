import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {
    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        int T, A, B, min, max, tmp;
        T = Integer.parseInt(br.readLine());
        for (int i = 0; i < T; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            A = Integer.parseInt(st.nextToken());
            B = Integer.parseInt(st.nextToken());
            
            if (A < B) {
                min = A;
                max = B;
            } else {
                min = B;
                max = A;
            }

            if (min == 1 || max == 1) sb.append(max * min).append('\n');
            else if (max % min == 0) sb.append(max).append('\n');
            else {
                tmp = max * min;
                for (int j = min-1; j > 0; j--) {
                    if (max % j == 0 && min % j == 0) {
                        tmp /= j;
                        sb.append(tmp).append('\n');
                        break;
                    }
                }
            }
        }

        bw.write(sb.toString());
        bw.flush();
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    } 
}