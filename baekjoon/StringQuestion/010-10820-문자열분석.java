import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;


public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        while (br.ready()) {
            int lowerCnt = 0, upperCnt = 0, numCnt = 0, emptyCnt = 0;
            char[] arrChar = br.readLine().toCharArray();
            for (int i = 0; i < arrChar.length; i++) {
                if (arrChar[i] >= 48 && arrChar[i] <= 57) numCnt++;
                else if (arrChar[i] >= 65 && arrChar[i] <= 90) upperCnt++;
                else if (arrChar[i] >= 97 && arrChar[i] <= 122) lowerCnt++;
                else if (arrChar[i] != 10) emptyCnt++;
            }
            sb.append(lowerCnt + " " + upperCnt + " " + numCnt + " " + emptyCnt + '\n');
        }
        bw.write(sb.toString());
        bw.flush();
        bw.close();
        br.close();
    }
}