import java.io.BufferedReader;
import java.io.InputStreamReader;


public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        String votes = br.readLine().replace("\n", "");
        int A = 0, B = 0;
        for (int i = 0; i < votes.length(); i++) {
            if (votes.charAt(i) == 'A') A++;
            else B++;  
        }

        if (A > B) System.out.print("A");
        else if (A == B) System.out.print("Tie");
        else System.out.print("B");
    }
}