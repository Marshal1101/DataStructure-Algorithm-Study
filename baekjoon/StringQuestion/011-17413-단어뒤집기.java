import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Stack;


public class Main {
    // Stack과 StringBuilder를 사용하여 Java에서 문자열을 반전시키는 메소드
    public static String reverse(String str) {
        // 기본 케이스: 문자열이 null이거나 비어 있는 경우
        if (str == null || str.equals("")) {
            return str;
        }
        // 빈 문자 Stack 생성
        Stack<Character> stack = new Stack<Character>();
        // 주어진 문자열의 모든 문자를 Stack에 푸시
        char[] ch = str.toCharArray();
        for (int i = 0; i < str.length(); i++) {
            stack.push(ch[i]);
        }
        // Stack에서 문자를 꺼내서 StringBuilder에 추가합니다.
        StringBuilder sb = new StringBuilder();
        while (!stack.isEmpty()) {
            sb.append(stack.pop());
        }
        // `StringBuilder`를 문자열로 변환하고 반환
        return sb.toString();
    }
    
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        
        String input = br.readLine();
        boolean angleBracketflag = false;
        int startIdx = 0, i = 0;
        for (; i < input.length(); i++) {
            char curChar = input.charAt(i);
            if (!angleBracketflag) {
                if (curChar == '<') {
                    sb.append(reverse(input.substring(startIdx, i)));
                    startIdx = i;
                    angleBracketflag = true;
                }
                
                else if (curChar == ' ') {
                    if (startIdx != i) {
                        sb.append(reverse(input.substring(startIdx, i)));
                    }
                    sb.append(" ");
                    startIdx = i+1;
                }
            }

            else {
                if (curChar == '>') {
                    sb.append(input.substring(startIdx, i+1));
                    startIdx = i + 1;
                    angleBracketflag = false;
                }
            }
        }

        if (startIdx != i) {
            sb.append(reverse(input.substring(startIdx, i)));
        }

        System.out.print(sb.toString());
    }
}