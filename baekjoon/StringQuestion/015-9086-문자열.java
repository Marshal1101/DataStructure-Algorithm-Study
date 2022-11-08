import java.io.BufferedReader;
import java.io.InputStreamReader;


public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        for (int i = 0; i < N; i++) {
            String input = br.readLine().replaceAll("\n", "");
            System.out.println(String.format("%c%c", input.charAt(0), input.charAt(input.length()-1)));
        }
    }
}