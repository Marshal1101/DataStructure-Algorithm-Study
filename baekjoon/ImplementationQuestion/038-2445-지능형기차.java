import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int maxCnt = 0;
        int curCnt = 0;
        for (int i = 0; i < 4; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            curCnt = curCnt - Integer.parseInt(st.nextToken()) + Integer.parseInt(st.nextToken());
            if (curCnt > maxCnt) maxCnt = curCnt;
        }

        System.out.println(maxCnt);
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}