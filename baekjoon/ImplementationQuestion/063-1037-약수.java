import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.util.StringTokenizer;

public class Main {
    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        int min = 1000000;
        int max = 0;
        int tmp;
        int T = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < T; i++) {
            tmp = Integer.parseInt(st.nextToken());
            if (tmp > max) max = tmp;
            if (tmp < min) min = tmp;
        }
    
        bw.write(String.valueOf(max*min));
        bw.flush();
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}