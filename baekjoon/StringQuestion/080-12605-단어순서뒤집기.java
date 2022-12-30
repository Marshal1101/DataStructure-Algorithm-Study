import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    public void solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringBuilder reversedSb = new StringBuilder();
        int N = Integer.parseInt(br.readLine());
        for (int i = 0; i < N; i++) {
            reversedSb.setLength(0);
            String[] line = br.readLine().split(" ");
            for (int j = line.length-1; j >= 0; j--) {
                reversedSb.append(" ").append(line[j]);
            }
            sb.append("Case #" + (i+1) +":"+ reversedSb).append("\n");
        }
        System.out.print(sb);
    }

    public static void main(String[] args) throws IOException {
        new Main().solution();
    }
}