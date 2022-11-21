import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.List;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        
        Character[] banned = new Character[]{'C', 'A', 'M', 'B', 'R', 'I', 'D', 'G', 'E'};
        List<Character> CList = new ArrayList<>(Arrays.asList(banned));

        String input = br.readLine().replace("\n", "");
        for (int i = 0; i < input.length(); i++) {
            if (!CList.contains(input.charAt(i))) {
                sb.append(input.charAt(i));
            }
        }
        System.out.print(sb);
    }
}