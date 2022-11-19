import java.io.BufferedReader;
import java.io.InputStreamReader;


public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        String convertedWord = br.readLine().replace("\n", "");
        for (int i = 0; i < convertedWord.length(); i++) {
            char origin = (char) (convertedWord.charAt(i) - 3);
            if (origin < 65) origin += 26;
            sb.append(origin);
        }

        System.out.print(sb);
    }
}