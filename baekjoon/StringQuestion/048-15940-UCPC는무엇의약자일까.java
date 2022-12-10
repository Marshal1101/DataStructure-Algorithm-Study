import java.io.BufferedReader;
import java.io.InputStreamReader;


public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        
        String input = br.readLine();
        for (int i = 0; i < input.length(); i++) {
            if (input.codePointAt(i) > 64 && input.codePointAt(i) < 91) {
                sb.append(input.charAt(i));
            }
        }

        String UCPC = "UCPC";
        int idx = 0;

        if (sb.length() > 3) {
            for (int i = 0; i < sb.length(); i++) {
                if (sb.charAt(i) == UCPC.charAt(idx)) {
                    idx++;
                    if (idx == 4) break;
                }
            }
        }
        
        if (idx == 4) System.out.print("I love UCPC");
        else System.out.print("I hate UCPC");
    }
}