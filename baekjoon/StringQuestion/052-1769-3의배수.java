import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;


public class Main {
    static int callCnt;

    public String getSumEachNum(String strNum) throws IOException {
        
        if (strNum.length() == 1) return strNum;
        callCnt++;
        
        long total = 0;
        for (int i = 0; i < strNum.length(); i++) {
            total += strNum.charAt(i) - '0';
        }
        
        return getSumEachNum(String.valueOf(total));
    }

    public void solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        callCnt = 0;

        int ret = Integer.parseInt(getSumEachNum(br.readLine()));

        if (ret % 3 == 0) {
            System.out.println(callCnt);
            System.out.println("YES");   
        }
        else {
            System.out.println(callCnt);
            System.out.println("NO");   
        }
    }

    public static void main(String[] args) throws IOException {
        new Main().solution();
    }
}