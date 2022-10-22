import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.OutputStreamWriter;
import java.io.BufferedWriter;
import java.util.StringTokenizer;


public class Main {
    public String reverse(String input) {
        char[] arr = input.toCharArray();
        char[] reversedArr = new char[arr.length];
        for (int k = 0; k < arr.length; k++) {
            reversedArr[arr.length-1-k] = arr[k];
        }

        return new String(reversedArr);
    }

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());
        for (int i = 0; i < T; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int N = st.countTokens();
            for (int j = 0; j < N; j++) {
                sb.append(reverse(st.nextToken()) + " ");
            }
            sb.append('\n');
        }

        bw.write(sb.toString());
        bw.flush();
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}