import java.io.BufferedReader;
import java.io.InputStreamReader;


public class Main {
    public int search(String src, String target) throws Exception {
        int count = 0;
        int begin = 0;
        while (begin + target.length() <= src.length()) {
            boolean matched = true;
            for (int i = 0; i < target.length(); i++) {
                if (src.charAt(begin + i) != target.charAt(i)) {
                    matched = false;
                    break;
                }
            }
            if (matched) {
                begin += target.length();
                count++;
            }
            else begin += 1;
        }

        return count;
    }

    public void soluton() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String src = br.readLine().replace("\n", "");
        String target = br.readLine().replace("\n", "");
        System.out.print(search(src, target));
    }

    public static void main(String[] args) throws Exception {
        new Main().soluton();
    }
}