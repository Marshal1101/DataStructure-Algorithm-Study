import java.io.BufferedReader;
import java.io.InputStreamReader;


public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        for (int i = 1; i <= 5; i++) {
            if (br.readLine().contains("FBI")) sb.append(i + " ");
        }

        if (sb.length() > 0) System.out.print(sb);
        else System.out.print("HE GOT AWAY!");
    }
}