import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    public void solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        String[] arr = new String[N];
        for (int i = 0; i < N; i++) {
            String curr_line = br.readLine();
            for (int k = 0; k < i; k++) {
                if (arr[k].equals(curr_line)) {
                    System.out.println(curr_line.length() +" "+ curr_line.charAt((int) curr_line.length()/2));
                    return;
                }
            }
            char[] currCharArr = curr_line.toCharArray();
            boolean isPelindrome = true;
            for (int j = 0; j < currCharArr.length/2; j++) {
                if (currCharArr[j] != currCharArr[currCharArr.length-1-j]) {
                    isPelindrome = false;
                }
                char temp = currCharArr[j];
                currCharArr[j] = currCharArr[currCharArr.length-1-j];
                currCharArr[currCharArr.length-1-j] = temp;
            }

            if (isPelindrome) {
                System.out.println(currCharArr.length +" "+ currCharArr[currCharArr.length/2]);
                return;
            }
            
            arr[i] = String.copyValueOf(currCharArr);
        }
    }

    public static void main(String[] args) throws IOException {
        new Main().solution();
    }
}