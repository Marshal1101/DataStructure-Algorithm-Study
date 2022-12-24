import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.io.IOException;
import java.util.StringTokenizer;


public class Main {
    public boolean canStrfry(String src, String target) {
        if (src.length() != target.length()) return false;

        int[] charCnt = new int[26];
        for (int j = 0; j < src.length(); j++) {
            charCnt[src.codePointAt(j)-97]++;
        }
        for (int j = 0; j < target.length(); j++) {
            charCnt[target.codePointAt(j)-97]--;
            if (charCnt[target.codePointAt(j)-97] < 0) {
                return false;
            }
        }

        return true;
    }

    public void solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(Sytem.out));
        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(br.readLine());
        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            if (canStrfry(st.nextToken(), st.nextToken())) {
                sb.append("Possible\n");
            }
            else {
                sb.append("Impossible\n");
            }
        }
        
        bw.write(sb.toString());
        bw.flush();
        br.close();
    }

    public static void main(String[] args) throws IOException {
        new Main().solution();
    }
}