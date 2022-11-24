import java.io.BufferedReader;
import java.io.InputStreamReader;


public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        char[] str1 = br.readLine().replace("\n", "").toCharArray();
        char[] str2 = br.readLine().replace("\n", "").toCharArray();
        int[][] dp = new int[str1.length][str2.length];

        int max = 0;
        for (int i = 0; i < str1.length; i++) {
            for (int j = 0; j < str2.length; j++) {
                if (str1[i] == str2[j]) {
                    if (i > 0 && j > 0 && dp[i-1][j-1] > 0) {
                        dp[i][j] += dp[i-1][j-1] + 1;
                        if (dp[i][j] > max) max = dp[i][j];
                    }
                    else dp[i][j] = 1;
                }
            }
        }

        System.out.print(max);
    }
}