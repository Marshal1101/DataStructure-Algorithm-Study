import java.io.BufferedReader;
import java.io.InputStreamReader;


public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N, prevIdx, cnt, cntW, cntH;
        N = Integer.parseInt(br.readLine());
        if (N == 1) System.out.print("0 0");
        else {
            char[][] line = new char[N][];

            cntW = 0;
            for (int i = 0; i < N; i++) {
                line[i] = br.readLine().toCharArray();
                cnt = 0; 
                prevIdx = -1;
                for (int j = 0; j < N; j++) {
                    if (line[i][j] == 'X') {
                        if (j - prevIdx > 2) cnt++;
                        prevIdx = j;
                    }
                }
                if (N - prevIdx > 2) cnt++;
                cntW += prevIdx > -1 ? cnt : 1;
            }

            cntH = 0;
            for (int j = 0; j < N; j++) {
                cnt = 0;
                prevIdx = -1;
                for (int i = 0; i < N; i++) {
                    if (line[i][j] == 'X') {
                        if (i - prevIdx > 2) cnt++;
                        prevIdx = i;
                    }
                }
                if (N - prevIdx > 2) cnt++;
                cntH += prevIdx > -1 ? cnt : 1;
            }

            System.out.print(cntW + " " + cntH);
        }
    }
}