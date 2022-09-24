import java.util.Scanner;

public class Main {
    public void solution() throws Exception {
        Scanner sc = new Scanner(System.in);
        int R1, S, R2;
        R1 = sc.nextInt();
        S = sc.nextInt();
        R2 = 2 * S - R1;
        System.out.println(R2);
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}