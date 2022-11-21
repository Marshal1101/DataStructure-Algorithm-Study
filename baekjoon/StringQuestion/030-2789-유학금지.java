import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int[] banned = {'C', 'A', 'M', 'B', 'R', 'I', 'D', 'G', 'E'};
        
        String input = br.readLine().replace("\n", "");
        for (int i = 0; i < input.length(); i++) {
            Boolean flag = true;
            for (int b: banned) {
                if (b == input.codePointAt(i)) {
                    flag = false;
                    break;
                }
            }
            if (flag) sb.append(input.charAt(i));
        }
        System.out.print(sb);
    }
}