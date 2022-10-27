import java.io.BufferedReader;
import java.io.InputStreamReader;


public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        char[] arrChar = br.readLine().toCharArray();
        for (int i = 0; i < arrChar.length; i++) {
            if (arrChar[i] < 91) {
                arrChar[i] += 32;
            }
            else {
                arrChar[i] -= 32;
            }
        }

        System.out.print(String.valueOf(arrChar));
    }
}