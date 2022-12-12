import java.io.InputStreamReader;
import java.io.BufferedReader;


public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int[] cnt = new int[26];

        String line = "";
        while ((line = br.readLine()) != null) {
            for (int i = 0; i < line.length(); i++) {
                if (line.charAt(i) != ' ') cnt[line.codePointAt(i)-97]++;
            }
        }
        
        int max = 0;
        for (int i = 0; i < cnt.length; i++) {
            if (cnt[i] > max) max = cnt[i];
        }

        for (int i = 0; i < cnt.length; i++) {
            if (cnt[i] == max) sb.append((char) (i + 97));
        }

        System.out.print(sb);
    }
}