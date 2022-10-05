import java.util.Scanner;


public class Main {
    public void solution() throws Exception {
        Scanner sc = new Scanner(System.in);
        int A = sc.nextInt();
        int I = sc.nextInt();
        
        System.out.println(A * (I - 1) + 1);
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}