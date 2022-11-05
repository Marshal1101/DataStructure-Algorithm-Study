import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashMap;

public class Main {
    public static void main(String[] args) throws Exception {
        HashMap<String, String> binaryTable = new HashMap<String, String>(){{
            put("000", "0");
            put("001", "1");
            put("010", "2");
            put("011", "3");
            put("100", "4");
            put("101", "5");
            put("110", "6");
            put("111", "7");
        }};

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder octIn = new StringBuilder(br.readLine());
        StringBuilder sb = new StringBuilder();
        int length = octIn.length();
        if (length % 3 == 2) octIn.insert(0, "0");
        else if (length % 3 == 1) octIn.insert(0, "00");
        
        for (int i = 0; i < octIn.length(); i+=3) {
            sb.append(binaryTable.get(octIn.substring(i, i+3)));
        }

        System.out.print(sb);
    }
}