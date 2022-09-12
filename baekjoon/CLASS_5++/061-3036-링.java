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

        int N, R, r, gcd, div, numerator, denominator;
        N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        R = Integer.parseInt(st.nextToken());
        for (int i = 0; i < N-1; i++) {
            r = Integer.parseInt(st.nextToken());
            gcd = GCD(R, r);
            div = R * r / gcd;
            numerator = div / r;
            denominator = div / R;
            sb.append(numerator + "/" + denominator).append('\n');
        }

        bw.write(sb.toString());
        bw.flush();
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}