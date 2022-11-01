import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;


public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        int maxLen = 0;
        char[] input;
        char[][] arrChar = new char[5][15];
        for (int i = 0; i < 5; i++) {
            input = br.readLine().toCharArray();
            for (int j = 0; j < input.length; j++) {
                arrChar[i][j] = input[j];
            }
            if (arrChar[i].length > maxLen) maxLen = arrChar[i].length;
        }

        for (int j = 0; j < maxLen; j++) {
            for (int i = 0; i < 5; i++) {
                if (arrChar[i][j] != 0) {
                    sb.append(arrChar[i][j]);
                }
            }
        }

        bw.write(sb.toString());
        bw.flush();
    }
}