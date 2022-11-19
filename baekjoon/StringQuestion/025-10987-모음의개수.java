import java.io.BufferedReader;
import java.io.InputStreamReader;


public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String word = br.readLine();
        int cnt = 0;
        for (int i = 0; i < word.length(); i++) {
            switch (word.charAt(i)) {
                case 'a': cnt++; break;
                case 'e': cnt++; break;
                case 'i': cnt++; break;
                case 'o': cnt++; break;
                case 'u': cnt++; break;
                default: break;
            }
        }
        System.out.print(cnt);
    }
}