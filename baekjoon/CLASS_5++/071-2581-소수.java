import java.io.InputStreamReader;
import java.io.BufferedReader;

public class Main {
    public int primeCheck(int num) throws Exception {
        if (num == 1) return 0;
        if (num == 2) return 1;
        int end = (int) Math.sqrt(num);
        for (int i = 2; i <= end; i++) {
            if (num % i == 0) return 0;
        }
        
        return 1;
    }

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int M = Integer.parseInt(br.readLine());
        int N = Integer.parseInt(br.readLine());
        int S = 0;
        int prev = -1;

        for (int i = N; i >= M; i--) {
            if (this.primeCheck(i) == 1) {
                S += i;
                prev = i;
            }
        }

        System.out.println(S > 0 ? S : -1);
        if (S > 0) System.out.println(prev);
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}