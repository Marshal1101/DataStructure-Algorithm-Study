import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(br.readLine());
        int L = 2 * N - 1;
        int starNum, emptyNum;
        for (int i = 0; i < N; i++) {
            starNum = L - (2*i);
            emptyNum = (L - starNum) / 2;
            String empty = " ".repeat(emptyNum);
            String star = "*".repeat(starNum);
            sb.append(empty).append(star).append('\n');
        }
        for (int i = 1; i < N; i++) {
            starNum = 2 * i + 1;
            emptyNum = (L - starNum) / 2;
            String empty = " ".repeat(emptyNum);
            String star = "*".repeat(starNum);
            sb.append(empty).append(star).append('\n');
        }

        System.out.println(sb);
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}