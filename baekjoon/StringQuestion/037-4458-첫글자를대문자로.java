import java.io.InputStreamReader;
import java.io.BufferedReader;


public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(br.readLine());
        String line;
        for (int i = 0; i < N; i++) {
            line = br.readLine();
            if (line.charAt(0) > 96) {
                sb.append((char) (line.charAt(0) - 32)).append(line.substring(1)).append("\n");
            } else {
                sb.append(line).append("\n");
            }
        }

        System.out.print(sb);
    }
}