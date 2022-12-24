import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


public class Main {
    public String CD(int num1, int num2) throws IOException {
        int n1, n2, tmp, cd1, cd2;
        if (num2 > num1) {
            n1 = num2;
            n2 = num1;
        } else {
            n1 = num1;
            n2 = num2;
        }

        while (n2 != 0) {
            tmp = n1 % n2;
            n1 = n2;
            n2 = tmp;
        }
        cd1 = num1 / n1;
        cd2 = num2 / n1;

        return cd1 + ":" + cd2;
    }

    public void solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st = new StringTokenizer(br.readLine(), ":");
        int num1 = Integer.parseInt(st.nextToken());
        int num2 = Integer.parseInt(st.nextToken());
        System.out.println(CD(num1, num2));
    }

    public static void main(String[] args) throws IOException {
        new Main().solution();
    }
}