import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;


public class Main {
    public int[] getPartialMatch(String search) {
        int M = search.length();
        int[] pi = new int[M];

        int begin = 1;
        int matched = 0;

        while (begin + matched < M) {
            if (search.charAt(begin + matched) == search.charAt(matched)) {
                matched++;
                pi[begin + matched - 1] = matched;
            }

            else {
                if (matched == 0) begin++;
                else {
                    begin += matched - pi[matched - 1];
                    matched = pi[matched - 1];
                }
            }
        }

        return pi;
    }

    public ArrayList<integer> KMP(String src, String search) {
        ArrayList<integer> ret = new ArrayList<integer>();
        int N = src.length();
        int M = search.length();

        pi = getPartialMatch(search);

        int begin = 0;
        int matched = 0;
        while (begin <= N - M) {
            if (matched < M && src.charAt(begin + matched) == search.charAt(matched)) {
                matched++;
                if (matched == M) ret.add(begin);
            }
            else {
                if (matched == 0) begin++;
                else {
                    begin += matched - pi[matched - 1];
                    matched = pi[matched - 1];
                }
            }
        }

        return ret;
    }

    public void soluton() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int L = Integer.parseInt(br.readLine());
        String str = br.readLine();
        int[] pi = getPartialMatch(str);
        System.out.print(L - pi[pi.length-1]);
    }

    public static void main(String[] args) throws Exception {
        new Main().soluton();
    }
}