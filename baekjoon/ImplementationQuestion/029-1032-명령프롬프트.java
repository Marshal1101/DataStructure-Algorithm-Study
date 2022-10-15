import java.io.InputStreamReader;
import java.io.BufferedReader;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(br.readLine());
        String[] arr = new String[N];
        for (int i = 0; i < N; i++) {
            arr[i] = br.readLine();
        }
        if (N == 1) System.out.print(arr[0]);
        else {
            for (int i = 0; i < arr[0].length(); i++) {
                boolean flag = false;
                for (int j = 1; j < N; j++) {
                    if (arr[0].charAt(i) != arr[j].charAt(i)) {
                        sb.append("?");
                        flag = true;
                        break;
                    }
                }
                if (!flag) sb.append(arr[0].substring(i, i+1));
            }

            System.out.print(sb.toString());
            br.close();
        }
    }
}