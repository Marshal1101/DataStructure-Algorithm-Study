import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for (int i = 0; i < T; i++) {
            String line = br.readLine();
            int total = 2015;
            boolean[] check = new boolean[26];
            for (int j = 0; j < line.length(); j++) {
                if (!check[line.codePointAt(j)-65]) {
                    total -= line.codePointAt(j);
                    check[line.codePointAt(j)-65] = true;
                }
            }

            System.out.println(total);
        }

        br.close();
    }
}