import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.io.IOException;
import java.util.StringTokenizer;


public class Main {
    public String crossWord(String src, String target) {
        // find indexes of the character matched
        int srcIdx = src.length(), targetIdx = target.length();
        int[] charCnt = new int[26];
        for (int i = 0; i < 26; i++) charCnt[i] = -1;
        for (int i = 0; i < src.length(); i++) {
            if (charCnt[src.codePointAt(i)-65] < 0) {
                charCnt[src.codePointAt(i)-65] = i;
            };
        }
        for (int j = 0; j < target.length(); j++) {
            if (charCnt[target.codePointAt(j)-65] != -1) {
                if (charCnt[target.codePointAt(j)-65] < srcIdx) {
                    srcIdx = charCnt[target.codePointAt(j)-65]; 
                    targetIdx = j;
                }
            }
        }

        // make a metrix with string for output
        StringBuilder ret = new StringBuilder();
        for (int i = 0; i < target.length(); i++) {
            if (i == targetIdx) {
                ret.append(src);
            }
            else {
                for (int j = 0; j < src.length(); j++) {
                    if (j != srcIdx) ret.append(".");
                    else ret.append(target.charAt(i));
                }
            } 
            ret.append('\n');
        }

        return ret.toString();
    }
    
    public void solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        bw.write(crossWord(st.nextToken(), st.nextToken()));
        bw.flush();
        br.close();
    }

    public static void main(String[] args) throws IOException {
        new Main().solution();
    }
}