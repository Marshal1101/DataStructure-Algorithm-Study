import java.util.Scanner;

public class Main {
    public void solution() throws Exception {
        Scanner sc = new Scanner(System.in);
        String input = sc.next();

        int[] count = new int[10];
        int maxCnt = 0, maxIdx = 0;
        for (int i = 0; i < 10; i++) count[i] = 0;        
        for (int i = 0; i < input.length(); i++) {
            int idx = Character.getNumericValue(input.charAt(i));
            count[idx]++;
            if (count[idx] > maxCnt && idx != 6 && idx != 9) {
                maxCnt = count[idx];
                maxIdx = idx;
            }
        }

        int sixNine = count[6] + count[9];
        if (sixNine % 2 == 0) sixNine = sixNine / 2;
        else sixNine = sixNine / 2 + 1;

        if (maxCnt > sixNine) System.out.println(maxCnt);
        else System.out.println(sixNine);
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}