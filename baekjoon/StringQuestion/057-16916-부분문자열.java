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

    public int KMP(String src, String search) {
        int N = src.length();
        int M = search.length();

        int[] pi = getPartialMatch(search);

        int begin = 0;
        int matched = 0;
        while (begin <= N - M) {
            if (matched < M && src.charAt(begin + matched) == search.charAt(matched)) {
                matched++;
                if (matched == M) return 1;
            }
            else {
                if (matched == 0) begin++;
                else {
                    begin += matched - pi[matched - 1];
                    matched = pi[matched - 1];
                }
            }
        }

        return 0;
    }

    public void soluton() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        System.out.println(KMP(br.readLine(), br.readLine()));
    }

    public static void main(String[] args) throws Exception {
        new Main().soluton();
    }
}