import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.IOException;

public class Main {
    public void solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int X = Integer.parseInt(br.readLine());
        int S = 0;
        int n = 0;
        do {
            n++;
            S += n;
        } while(S < X);
        
        int gap = S - X;
        if (gap == 0) {
            if (n % 2 > 0) System.out.println("1/" + n);
            else System.out.println(n + "/1");
        } else {
            String d = String.valueOf(n - gap) ;
            String u = String.valueOf(1 + gap);
            if (n % 2 > 0) System.out.println(u + '/' + d);    
            else System.out.println(d + '/' + u);
        }
    }
    
    public static void main(String[] args) throws IOException {
        new Main().solution();
    }
}