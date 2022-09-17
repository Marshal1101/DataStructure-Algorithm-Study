import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.util.StringTokenizer;
import java.util.HashSet;

public class Main {
    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine();

        HashSet<String> result = new HashSet<>();
        
        int N = input.length();
        String[] arr = new String[N];
        String curChar;
        for (int i = 0; i < N; i++) {
            curChar = input.substring(i, i+1);
            for (int j = i; j >= 0; j--) {
                arr[j] += curChar;
                result.add(arr[j]);
            }
        }

        System.out.print(result.size());
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}