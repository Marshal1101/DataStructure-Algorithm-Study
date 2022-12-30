// https://www.acmicpc.net/source/51389153

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        HashMap<String, String> map = new HashMap<>();
        StringBuffer sb;
        int n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) {
            String str = br.readLine();
            sb = new StringBuffer(str);
            String reversedStr = sb.reverse().toString();
            if (str.equals(reversedStr) || map.containsKey(reversedStr)) {
                bw.append(String.valueOf(str.length())).append(" ").append(String.valueOf(str.charAt(str.length() / 2)));
                break;
            }
            map.put(str, reversedStr);
        }

        bw.flush();
        bw.close();
    }
}