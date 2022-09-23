import java.util.Scanner;

public class Main {
    public void solution() throws Exception {
        Scanner sc = new Scanner(System.in);

        int N, a1, a2, a3, cnt;
        N = sc.nextInt();
        
        if (N == 1 || N == 2) {
            System.out.println(1);
        } else {
            cnt = 2; a1 = 0; a2 = 1; a3 = 1;
            while (cnt < N) {
                a1 = a2;
                a2 = a3;
                a3 = a1 + a2;
                cnt++;
            }
            System.out.println(a3);
        }
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}