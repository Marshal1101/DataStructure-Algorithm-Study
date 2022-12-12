import java.io.BufferedReader;
import java.io.InputStreamReader;


public class Main{
    public int recursion(String s, int l, int r, int cnt) throws Exception {
        if(l >= r) return cnt+1;
        else if(s.charAt(l) != s.charAt(r)) return -(cnt+1);
        else return recursion(s, l+1, r-1, cnt+1);
    }
    public int isPalindrome(String s) throws Exception {
        return recursion(s, 0, s.length()-1, 0);
    }
    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(br.readLine());
        for (int i = 0; i < N; i++) {
            int cnt = isPalindrome(br.readLine());
            if (cnt > 0) sb.append("1 " + cnt + "\n");
            else sb.append("0 " + -cnt + "\n");
        }

        System.out.print(sb);
    }
    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}