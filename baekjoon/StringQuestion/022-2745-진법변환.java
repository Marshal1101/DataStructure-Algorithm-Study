import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        String num = st.nextToken();
        int N = Integer.parseInt(st.nextToken());

        int deciVal = 0;
        for (int i = 0; i < num.length(); i++) {
            int curAscii = num.charAt(i);
            if (curAscii > 58) {
                deciVal += (num.charAt(i) - 55) * (int)Math.pow(N, num.length()-1-i);
            } else {
                deciVal += (num.charAt(i) - 48) * (int)Math.pow(N, num.length()-1-i);
            }
        }


        System.out.print(deciVal);
    }
}