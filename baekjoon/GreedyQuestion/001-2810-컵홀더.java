import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int cnt = 0;
        String seat = br.readLine().replace("\n", "");
        char curr, prev = 'S', hand = 'L';
        for (int i = 0; i < N; i++) {
            curr = seat.charAt(i);
            if (hand == 'L') {
                if (prev == 'S') {
                    cnt += 1;
                    prev = curr;
                }
                else if (prev == 'L') {
                    cnt += 1;
                    prev = 0;
                    hand = 'R';
                }
            }
            else {
                if (prev == 0 || prev == 'S') {
                    if (curr == 'S') cnt += 1;
                    prev = curr;
                }
                else if (prev == 'L') {
                    cnt += 1;
                    prev = 0;
                }
            }
        }
        System.out.print(cnt);
    }
}