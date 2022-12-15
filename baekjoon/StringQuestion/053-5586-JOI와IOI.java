import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.IOException;


public class Main {
    public int getCntBruteForceSearch(String src, String target) throws IOException {
        int count = 0;
        int begin = 0;
        while (begin + target.length() <= src.length()) {
            boolean matched = true;
            for (int i = 0; i < target.length(); i++) {
                if (src.charAt(begin + i) != target.charAt(i)) {
                    matched = false;
                    break;
                }
            }
            if (matched) count++;
            begin += 1;
        }

        return count;
    }
    
    public void solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String src = br.readLine();
        System.out.println(getCntBruteForceSearch(src, "JOI"));
        System.out.println(getCntBruteForceSearch(src, "IOI"));
    }


    public static void main(String[] args) throws IOException {
        new Main().solution();
    }
}