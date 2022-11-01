import java.io.BufferedReader;
import java.io.InputStreamReader;


public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        String[] arr = br.readLine().split(" ");
        long result = Long.parseLong(arr[0] + arr[1]) + Long.parseLong(arr[2] + arr[3]);

        System.out.print(result);
    }
}