import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    public boolean checkVowel(char c) throws IOException {
        char[] vowel = {'a', 'e', 'i', 'o', 'u'};
        for (int i = 0; i < vowel.length; i++) {
            if (c == vowel[i]) return true;
        }
        return false;
    }

    public boolean pwdCheck(String pwd) throws IOException {
        boolean hasVowel = false, isPrevVowel;
        char prev = pwd.charAt(0), curr = 0;
        int equalTypeCnt = 0;

        if (checkVowel(prev)) {
            hasVowel = true;
            isPrevVowel = true;
            equalTypeCnt = 1;
        }
        else {
            isPrevVowel = false;
            equalTypeCnt = -1;
        }

        for (int i = 1; i < pwd.length(); i++) {
            curr = pwd.charAt(i);
            
            if (checkVowel(curr)) {
                hasVowel = true;
                if (isPrevVowel) equalTypeCnt++;
                else equalTypeCnt = 1;
                isPrevVowel = true;
            }
            else {
                if (isPrevVowel) equalTypeCnt = -1;
                else equalTypeCnt--;
                isPrevVowel = false;
            }

            if (curr == prev && curr != 'e' && curr != 'o') {
                return false;
            }

            if (equalTypeCnt == 3 || equalTypeCnt == -3) {
                return false;
            }

            prev = curr;
        }

        if (hasVowel) return true;
        else return false;
    }
    
    public void solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String input;
        while (true) {
            input = br.readLine();
            if (input.equals("end")) break;
            if (pwdCheck(input)) System.out.println("<"+input+"> is acceptable.");
            else System.out.println("<"+input+"> is not acceptable.");
        }
        br.close();
    }

    public static void main(String[] args) throws IOException {
        new Main().solution();
    }
}