import java.util.Scanner;


public class Main {
    public void solution() throws Exception {
        Scanner sc = new Scanner(System.in);
        char[] arr = sc.next().toCharArray();
        int[] cnt = new int[2];
        char prev = ' ';
        for (int i = 0; i < arr.length; i++) {
            if (prev != arr[i]) {
                prev = arr[i];
                cnt[arr[i]-48]++;
            }
        }

        System.out.print(cnt[0] < cnt[1] ? cnt[0] : cnt[1]);
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}