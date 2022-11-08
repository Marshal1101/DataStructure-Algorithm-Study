import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


public class Main {

    public void soluton() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        String strA = st.nextToken();
        String strB = st.nextToken();
        int i, j, cnt, minCnt = strA.length();
        for (i = 0; i < strB.length()-strA.length()+1; i++) {
            cnt = 0;
            for (j = 0; j < strA.length(); j++) {
                if (strA.charAt(j) != strB.charAt(i+j)) cnt++;
            }
            if (cnt < minCnt) minCnt = cnt; 
        }
        System.out.print(minCnt);
    }

    public static void main(String[] args) throws Exception {
        new Main().soluton();
    }
}