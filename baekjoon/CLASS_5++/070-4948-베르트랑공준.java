import java.io.InputStreamReader;
import java.io.BufferedReader;

public class Main {
    public static boolean[] prime = new boolean[246913];
    

    public boolean primeCheck(int num) throws Exception {
        if (num == 1) return false;
        if (num == 2) return true;
        int end = (int) Math.sqrt(num);
        for (int i = 2; i <= end; i++) {
            if (num % i == 0) return false;
        }
        
        return true;
    }

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        prime[0] = prime[1] = true;
        int n = Integer.parseInt(br.readLine());
        while (n != 0) {
            int count = 0;
            for (int i = n+1; i <= 2*n; i++) {
                if (this.primeCheck(i) == true) count++; 
            }
            System.out.println(count);

            n = Integer.parseInt(br.readLine());
        }
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}