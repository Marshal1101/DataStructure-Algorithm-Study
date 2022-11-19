import java.io.BufferedReader;
import java.io.InputStreamReader;


public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String vovels = "aeiouAEIOU";
        
        String line = br.readLine();
        while (line.charAt(0) != '#') {
            int cnt = 0;
            for (int i = 0; i < line.length(); i++) {
                if (vovels.contains(Character.toString(line.charAt(i)))) cnt++;
            }
            System.out.println(cnt);
            line = br.readLine();
        }
    }
}