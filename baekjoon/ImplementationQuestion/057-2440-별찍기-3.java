import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {
    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(br.readLine());
        String star = "";
        for (int i = N; i > 0; i--) {
            for (int j = 0; j < i; j++) {
                star += "*";
            }
            sb.append(star).append('\n');
            star = "";
        }
        
        bw.write(sb.toString());
        bw.flush();
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}