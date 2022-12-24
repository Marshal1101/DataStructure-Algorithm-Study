/**
n i Eng
0 8 e
1 5 fi
2 4 fo
3 9 n
4 1 o
5 7 se
6 6 si
7 3 th
8 2 tw
9 0 z

 */
import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;
import java.util.Arrays;


public class Main {
    static char[] table = {'9', '4', '8', '7', '2', '1', '6', '5', '0', '3'};

    public String convertIntToEng(int num) {
        StringBuilder ret = new StringBuilder();
        String tmp = String.valueOf(num);
        for (int i = 0; i < tmp.length(); i++) {
            ret.append(table[tmp.charAt(i) - '0']);
        }

        return ret.toString();
    }

    public String convertEngToStr(String num) {
        StringBuilder ret = new StringBuilder();
        for (int i = 0; i < num.length(); i++) {
            for (int j = 0; j < table.length; j++) {
                if (num.charAt(i) == table[j]) {
                    ret.append(j);
                    break;
                }
            }
        }
        return ret.toString();
    }

    public String[] arrbyEngName(String M, String N) {
        int start = Integer.parseInt(M);
        int end = Integer.parseInt(N);
        String[] arr = new String[end - start + 1];
        for (int i = start; i <= end; i++) {
            arr[i-start] = convertIntToEng(i);
        }
        Arrays.sort(arr);
        for (int i = 0; i < arr.length; i++) {
            arr[i] = convertEngToStr(arr[i]);
        }
        
        return arr;
    }

    public void solution() throws IOException {
        StringBuilder ans = new StringBuilder();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        String M = st.nextToken();
        String N = st.nextToken();
        String[] arr = arrbyEngName(M, N);
        for (int i = 0; i < arr.length; i++) {
            if (i != 0 && i % 10 == 0) bw.write('\n');
            bw.write(arr[i] + " ");
        }

        bw.flush();
        br.close();
    }

    public static void main(String[] args) throws IOException {
        new Main().solution();    
    }
}
