import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;


public class Main {
    public static boolean checkYujin(char[] num) throws IOException {
        if (num.length == 1) return false;

        int cnt = 0;
        for (int i=0; i<num.length; i++) {
            if (num[i] == '0' && ++cnt > 1) return true;
        }
        if (cnt == 1) return false;
        
        int rightVal = 1;
        for (int i=0; i<num.length; i++) {
            rightVal *= num[i] - '0';
        }

        int leftVal = 1;
        for (int i=0; i<num.length; i++) {
            leftVal *= num[i] - '0';
            rightVal /= num[i] - '0';
            if (leftVal == rightVal) {
                return true;
            }
        }

        return false;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        if (checkYujin(br.readLine().toCharArray())) System.out.println("YES");
        else System.out.println("NO");
    }
}