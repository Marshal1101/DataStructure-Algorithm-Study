import java.io.InputStreamReader;
import java.io.BufferedReader;

public class Main {
    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int tmp = N;
        int cnt = 0;
        int a, b, c;
        do {
            a = tmp / 10;
            b = tmp % 10;
            c = 0;
            if (a >= 1) c = a + b;
            else c = b;
            tmp = b * 10 + c % 10;
            cnt++;
        } while (tmp != N);

        System.out.print(cnt);
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}