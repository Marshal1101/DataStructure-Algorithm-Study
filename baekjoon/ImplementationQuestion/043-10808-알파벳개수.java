import java.util.Scanner;

public class Main {
    public void solution() throws Exception {
        StringBuilder sb = new StringBuilder();
        Scanner sc = new Scanner(System.in);
        String input = sc.next();
        int[] count = new int[26];
        for (int i = 0; i < 26; i++) count[i] = 0;
        for (int i = 0; i < input.length(); i++) {
            int ascNum = (int) input.charAt(i);
            count[ascNum - 97]++;
        }
        for (int i = 0; i < 26; i++) {
            sb.append(count[i] + " ");
        }
        System.out.println(sb);
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}