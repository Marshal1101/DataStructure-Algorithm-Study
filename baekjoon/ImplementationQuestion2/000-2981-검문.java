import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

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

        int N, i, min1, min2, tmp, rest, num;
        min1 = 1000000000;
        min2 = 1000000000;
        N = Integer.parseInt(br.readLine());
        int[] arr = new int[N];
        for (i = 0; i < N; i++) {
            num = Integer.parseInt(br.readLine());
            arr[i] = num;
            if (num < min1) {
                min2 = min1;
                min1 = num;
            } else if (num < min2) {
                min2 = num;
            }
        }

        if (2 * min1 < min2) {
            min2 = 2*min1;
        }

        for (int k = 2; k < min2; k++) {
            rest = arr[0] % k;
            for (i = 1; i < N; i++) {
                tmp = arr[i] % k;
                if (tmp != rest) break;
            }
            if (i == N) sb.append(k).append(" "); 
        }

        bw.write(sb.toString());
        bw.flush();
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}