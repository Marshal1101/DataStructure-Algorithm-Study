import java.util.Scanner;


public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        String input = sc.next();
        int N, num, dec;
        N = input.length();
        dec = 0;
        for (int i = 0; i < N; i++) {
            num = Character.getNumericValue(input.charAt(i));
            dec += num * Math.pow(16, N-1-i);
        }

        System.out.println(dec);
    }
}