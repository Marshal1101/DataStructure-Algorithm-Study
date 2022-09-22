import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {
    public String makeStar(int N) throws Exception {
        if (N < 1) return "";
        if (N == 1) return "*";

        if (N % 2 == 0) {
            return makeStar(N/2) + makeStar(N/2);
        } else {
            return "*" + makeStar(N-1);
        }
    }

    public String makeEmpty(int N) throws Exception {
        if (N < 1) return "";
        if (N == 1) return " ";

        if (N % 2 == 0) {
            return makeEmpty(N/2) + makeEmpty(N/2);
        } else {
            return " " + makeEmpty(N-1);
        }
    }
    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();
        
        int N = Integer.parseInt(br.readLine());
        int L = 2 * N - 1;
        for (int i = 1; i <= N; i++) {
            int starNum = 2 * i - 1;
            int emptyNum = (L - starNum) / 2;
            String empty = makeEmpty(emptyNum);
            String star = makeStar(starNum);
            sb.append(empty);
            sb.append(star).append('\n');
        }

        bw.write(sb.toString());
        bw.flush();
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}