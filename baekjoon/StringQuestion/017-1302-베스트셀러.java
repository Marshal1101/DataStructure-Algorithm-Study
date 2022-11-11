import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashMap;

public class Main {
    public static String stringSort(String str1, String str2) throws Exception {
        int shortL;
        String ret;
        if (str1.length() < str2.length()) {
            shortL = str1.length();
            ret = str1;
        }
        else {
            shortL = str2.length();
            ret = str2;
        }
        for (int i = 0; i < shortL; i++) {
            if (str1.charAt(i) - '0' < str2.charAt(i) - '0') return str1;
            if (str1.charAt(i) - '0' > str2.charAt(i) - '0') return str2;
        }
        return ret;
    } 

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        HashMap<String, Integer> map = new HashMap<>();
        String curBook, maxSellBook;
        int N, cnt, maxSellCnt;
        
        N = Integer.parseInt(br.readLine());
        curBook = br.readLine().replace("\n", "");
        map.put(curBook, 1);
        maxSellBook = curBook;
        maxSellCnt = 1;
        for (int i = 1; i < N; i++) {
            curBook = br.readLine().replace("\n", "");
            if (map.containsKey(curBook)) {
                cnt = map.remove(curBook);
                map.put(curBook, ++cnt);
            }
            else {
                map.put(curBook, 1);
            }
            if (map.get(curBook) > maxSellCnt) {
                maxSellCnt = map.get(curBook);
                maxSellBook = curBook;
            }
            else if (map.get(curBook) == maxSellCnt && curBook != maxSellBook) {
                maxSellBook = stringSort(curBook, maxSellBook);
            }
        }

        System.out.print(maxSellBook);
    }
}