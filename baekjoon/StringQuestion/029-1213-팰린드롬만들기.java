import java.io.BufferedReader;
import java.io.InputStreamReader;


public class Main {
    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        
        int[] alphaArr = new int[26];
        for (int i = 0; i < alphaArr.length; i++) alphaArr[i] = 0;

        String input = br.readLine();
        int N = input.length();
        char[] ret = new char[N];
        for (int i = 0; i < N; i++) {
            alphaArr[input.charAt(i) - 65]++;
        }
        
        int oddCnt = 0;
        for (int i = 0; i < alphaArr.length; i++) {
            if (alphaArr[i] % 2 != 0) {
                oddCnt++;
            }
        }

        if (oddCnt > 1) {
            System.out.print("I'm Sorry Hansoo");
            return;
        }

        int k = 0;
        for (int i = 0; i < alphaArr.length; i++) {
            int cnt = alphaArr[i];
            if (cnt % 2 != 0) {
                ret[N/2] = (char) (i + 65);
                cnt--;
            }
            while (cnt != 0) {
                ret[k] = (char) (i + 65);
                ret[N-1-k] = (char) (i + 65);
                cnt -= 2;
                k++;
            }
        }
        for (int i = 0; i < N; i++) {
            sb.append(ret[i]);
        }

        System.out.print(sb);
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}