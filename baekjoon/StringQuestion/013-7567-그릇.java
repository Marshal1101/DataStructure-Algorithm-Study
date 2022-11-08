import java.io.BufferedReader;
import java.io.InputStreamReader;


public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder input = new StringBuilder(br.readLine());
        char prev = 0; int height = 0;
        for (int i = 0; i < input.length(); i++) {
            if (prev != input.charAt(i)) {
                height += 10;
                prev = input.charAt(i);
            } 
            else {
                height += 5;
            }
        }

        System.out.print(height);
    }
}