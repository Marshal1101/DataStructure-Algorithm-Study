import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.Stack;

public class Main {
    public String rev(String str) throws Exception {
        if (str == null || str.equals("")) {
            return str;
        }

        Stack<Character> stack = new Stack<Character>();

        char[] ch = str.toCharArray();
        for (int i = 0; i < str.length(); i++) {
            stack.push(ch[i]);
        }

        StringBuilder sb = new StringBuilder();
        while (!stack.isEmpty()) {
            sb.append(stack.pop());
        }

        return sb.toString();
    }

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        String num1 = st.nextToken();
        String num2 = st.nextToken();
        int sum = Integer.parseInt(rev(num1)) + Integer.parseInt(rev(num2));
        String result = rev(Integer.toString(sum));
        System.out.print(Integer.parseInt(result));
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}