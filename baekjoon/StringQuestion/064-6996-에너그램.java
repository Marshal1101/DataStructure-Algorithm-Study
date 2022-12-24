import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public boolean anagramCheck(String src, String target) throws IOException {
        if (src.length() != target.length()) return false;
        
        int[] alphabetCnt = new int[26];
        for (int i = 0; i < src.length(); i++) {
            alphabetCnt[src.codePointAt(i)-97]++;
        }
        for (int i = 0; i < target.length(); i++) {
            alphabetCnt[target.codePointAt(i)-97]--;
        }
        for (int i = 0; i < 26; i++) {
            if (alphabetCnt[i] != 0) return false;
        }

        return true;
    }

    public void solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int T = Integer.parseInt(br.readLine());
        for (int i = 0; i < T; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String A = st.nextToken();
            String B = st.nextToken();
            if (anagramCheck(A, B)) sb.append(""+A+" & "+B+" are anagrams.\n");
            else sb.append(""+A+" & "+B+" are NOT anagrams.\n");
        }

        System.out.println(sb);
        br.close();
    }

    public static void main(String[] args) throws IOException {
        new Main().solution();
    }
}