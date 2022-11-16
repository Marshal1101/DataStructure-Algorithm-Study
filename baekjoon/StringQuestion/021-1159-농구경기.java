import java.io.BufferedReader;
import java.io.InputStreamReader;


public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int[] lastNameCnt = new int[26];
        for (int i = 0; i < 26; i++) lastNameCnt[i] = 0;
        int N = Integer.parseInt(br.readLine());
        for (int i = 0; i < N; i++) {
            lastNameCnt[br.readLine().charAt(0) - 'a']++;
        }

        for (int i = 0; i < 26; i++) {
            if (lastNameCnt[i] > 4) sb.append(String.valueOf((char) (i+'a')));
        }

        if (sb.length() > 0) System.out.print(sb);
        else System.out.print("PREDAJA");
    }
}