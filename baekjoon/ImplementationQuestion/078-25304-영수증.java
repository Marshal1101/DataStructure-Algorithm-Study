import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.util.StringTokenizer;
import java.io.IOException;

public class Main {
    public void solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int sum = 0;
        int total = Integer.parseInt(br.readLine());
        int N = Integer.parseInt(br.readLine());
        for (int i = 0; i < N; i++) {
            StringTokenizer stuff = new StringTokenizer(br.readLine());
            sum += Integer.parseInt(stuff.nextToken()) * Integer.parseInt(stuff.nextToken());
        }

        if (sum == total) System.out.print("Yes");
        else System.out.print("No");
    }

    public static void main(String[] args) throws IOException {
        new Main().solution();
    }
}