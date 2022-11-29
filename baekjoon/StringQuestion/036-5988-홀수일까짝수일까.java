import java.io.BufferedReader;
import java.io.InputStreamReader;


public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int N = Integer.parseInt(br.readLine());
        for (int i = 0; i < N; i++) {
            String num = br.readLine();
            if ((num.charAt(num.length()-1) - '0') % 2 == 0) {
                sb.append("even\n");
            } else {
                sb.append("odd\n");
            }
        }

        System.out.print(sb);
    }
}