import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.util.StringTokenizer;

public class Main {
    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < 3; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int frontCnt = 0;
            for (int j = 0; j < 4; j++) {
                int result = Integer.parseInt(st.nextToken());
                if (result == 0) frontCnt++; 
            }
            if (frontCnt == 1) sb.append('A').append('\n'); 
            else if (frontCnt == 2) sb.append('B').append('\n'); 
            else if (frontCnt == 3) sb.append('C').append('\n'); 
            else if (frontCnt == 4) sb.append('D').append('\n');
            else sb.append('E').append('\n');
        }

        bw.write(sb.toString());
        bw.flush();
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}