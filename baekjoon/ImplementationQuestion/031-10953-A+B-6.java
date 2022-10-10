import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        StringBuilder sb = new StringBuilder();
        int T = Integer.parseInt(sc.nextLine());
        for (int i = 0; i < T; i++) {
            String[] AB = sc.nextLine().split(",");
            sb.append(Integer.parseInt(AB[0]) + Integer.parseInt(AB[1])).append("\n");
        }

        System.out.println(sb);
    }
}