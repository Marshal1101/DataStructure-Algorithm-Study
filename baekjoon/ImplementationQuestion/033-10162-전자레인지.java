import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int T, A, B, C, cntA, cntB, cntC, temp;
        A = 300; B = 60; C = 10;
        cntA = 0; cntB = 0; cntC = 0;
        T = sc.nextInt();

        cntA = T / A;
        temp = T % A;
        if (temp != 0) {
            cntB = temp / B;
            temp = T % B;
        }
        if (temp != 0) {
            cntC = temp / C;
            temp = T % C;
        }
        if (temp != 0) System.out.println(-1);
        else System.out.printf("%d %d %d", cntA, cntB, cntC);
    }
}