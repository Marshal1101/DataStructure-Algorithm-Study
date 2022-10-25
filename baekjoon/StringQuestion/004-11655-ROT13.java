import java.io.BufferedReader;
import java.io.InputStreamReader;


public class Main {
    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        char[] arrChar = br.readLine().toCharArray();
        for (int i = 0; i < arrChar.length; i++) {
            int ascii = arrChar[i] - 0;
            if (ascii < 91 && ascii > 64) {
                ascii -= 65;
                ascii += 13;
                ascii %= 26;
                ascii += 65;
                arrChar[i] = (char) ascii;
            }
            else if (ascii > 96 && ascii < 123) {
                ascii -= 97;
                ascii += 13;
                ascii %= 26;
                ascii += 97;
                arrChar[i] = (char) ascii;
            }
        }

        System.out.print(String.valueOf(arrChar));
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}