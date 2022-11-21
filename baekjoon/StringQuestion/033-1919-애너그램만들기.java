import java.io.BufferedReader;
import java.io.InputStreamReader;


public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] alphabet = new int[26];

        String str1 = br.readLine();
        for (int i = 0; i < str1.length(); i++) {
            alphabet[str1.charAt(i)-97]++;
        }

        String str2 = br.readLine();
        for (int i = 0; i < str2.length(); i++) {
            alphabet[str2.charAt(i)-97]--;
        }

        int delCnt = 0;
        for (int i = 0; i < 26; i++) {
            delCnt += Math.abs(alphabet[i]);
        }

        System.out.print(delCnt);
    }
}