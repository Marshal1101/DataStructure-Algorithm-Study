import java.util.Scanner;


public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        StringBuilder sb = new StringBuilder();
        String[] names = sc.next().split("-");
        for (int i = 0; i < names.length; i++) {
            sb.append(names[i].charAt(0));
        }
        System.out.print(sb.toString());
        sc.close();
    }
}