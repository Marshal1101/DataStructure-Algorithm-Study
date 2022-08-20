import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] s = br.readLine().split(" ");
		int answer = 0;
		int count = 0;
        int max = Integer.parseInt(s[0]);
        int val = 0;
		for(int i=0; i < 3; i++) {
            if (count == 2) break;
            int before = Integer.parseInt(s[i]);
            for(int j=i+1; j < 3; j++) {
                int cur = Integer.parseInt(s[j]);
                if (cur > max) max = cur;
                if (before == cur) {
                    count = count + 1;
                    val = cur;
                }
            }
        }

        if (count == 2) {
            answer = 10000 + val * 1000;
        }
        else if (count == 1) {
            answer = 1000 + val * 100;
        }
        else {
            answer = 100 * max;
        }

		System.out.print(answer);
	}
}