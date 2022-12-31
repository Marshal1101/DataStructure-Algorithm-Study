import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        String pwd = br.readLine();
        int N = pwd.length();
        
        int R = 0;
        for (int i=1; i<(int)Math.sqrt(N)+1; i++) {
            if (N % i == 0) R = i;
        }

        int C = N / R;
        for (int i=0; i<R; i++) {
            for (int j=i; j<N; j+=R) {
                sb.append(pwd.charAt(j));
            }
        }

        System.out.println(sb);
    }
}