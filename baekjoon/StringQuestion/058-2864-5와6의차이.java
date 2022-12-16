import java.util.Scanner;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        char[] A = sc.next().toCharArray();
        char[] B = sc.next().toCharArray();

        for (int i = 0; i < A.length; i++) {
            if (A[i] == '5') A[i] = '6';   
        }
        for (int i = 0; i < B.length; i++) {
            if (B[i] == '5') B[i] = '6';
        }
        int maxSum = Integer.parseInt(String.copyValueOf(A)) + Integer.parseInt(String.copyValueOf(B));

        for (int i = 0; i < A.length; i++) {
            if (A[i] == '6') A[i] = '5';   
        }
        for (int i = 0; i < B.length; i++) {
            if (B[i] == '6') B[i] = '5';
        }
        int minSum = Integer.parseInt(String.copyValueOf(A)) + Integer.parseInt(String.copyValueOf(B));

        System.out.println(minSum + " " + maxSum);
    }
}