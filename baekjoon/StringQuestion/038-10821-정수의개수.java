import java.io.BufferedReader;
import java.io.InputStreamReader;


public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String input = br.readLine();
        int cnt = 0;
        for (int i = 0; i < input.length(); i++) {
            if (input.charAt(i) == ',') cnt++;
        }

        System.out.print(cnt+1);
    }
}