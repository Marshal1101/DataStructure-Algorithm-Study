import java.io.BufferedReader;
import java.io.InputStreamReader;


public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String input = br.readLine();
        int frontSum = 0, endSum = 0;
        for (int i = 0; i < input.length()/2; i++) {
            frontSum += input.charAt(i) - '0';
        }
        for (int i = input.length()/2; i < input.length(); i++) {
            endSum += input.charAt(i) - '0';
        }

        if (frontSum == endSum) System.out.print("LUCKY");
        else System.out.print("READY");
    }
}