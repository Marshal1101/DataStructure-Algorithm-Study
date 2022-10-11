import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int cnt = 0;
        for (int i = 0; i < 8; i++) {
            char[] arr = br.readLine().toCharArray();
            for (int j = 0; j < 8; j++) {
                if (i % 2 == 0 && j % 2 == 0 && arr[j] == 'F') cnt++;
                if (i % 2 != 0 && j % 2 != 0 && arr[j] == 'F') cnt++;
            }
        }

        System.out.println(cnt);
    }
}