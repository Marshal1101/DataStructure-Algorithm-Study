import java.util.Scanner;

public class Main {
    public void solution() throws Exception {
        Scanner sc = new Scanner(System.in);
        int tmp, max1, max2;
        max1 = max2 = 0;
        for (int i = 0; i < 3; i++) {
            tmp = sc.nextInt();
            if (tmp > max1) {
                max2 = max1;
                max1 = tmp;
            } else if (tmp > max2) {
                max2 = tmp;
            }
        }

        System.out.println(max2);
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}