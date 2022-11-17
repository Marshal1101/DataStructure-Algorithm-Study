import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;


public class Main {
    public String reverse(String str) throws IOException {
        if (str == null || str.equals("")) return str;

        StringBuilder ret = new StringBuilder();
        for (int i = str.length()-1; i >= 0; i--) {
            ret.append(str.charAt(i));
        }

        return ret.toString();
    }

    public void soluton() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        String line = br.readLine().replace("\n", "");
        while (true) {
            if (line.charAt(0) == 'E' && line.charAt(1) == 'N' && line.charAt(2) == 'D') {
                break;
            }
            String revStr = reverse(line);
            sb.append(revStr).append("\n");
            line = br.readLine().replace("\n", "");
        }

        System.out.print(sb);
    }

    public static void main(String[] args) throws IOException {
        new Main().soluton();
    }
}