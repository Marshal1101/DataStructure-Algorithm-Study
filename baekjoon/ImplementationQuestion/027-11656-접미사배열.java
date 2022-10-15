import java.util.Scanner;
import java.util.Arrays;


public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        String input = sc.next();

        int N = input.length();
        String[] arr = new String[N];
        for (int i = 0; i < N; i++) {
            arr[i] = input.substring(i, N);
        }

        Arrays.sort(arr);
        for (int i = 0; i < N; i++) {
            System.out.println(arr[i]);
        }
    }
}