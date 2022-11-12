import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        StringBuilder sb = new StringBuilder();

        int lenA, lenB, opt;
        String strA, strB, plusPrefix;
        strA = sc.next();
        lenA = strA.length();
        opt = sc.next().charAt(0);
        strB = sc.next();
        lenB = strB.length();

        if (opt == '+') {
            if (lenA > lenB) {
                plusPrefix = strA.substring(0, (lenA - lenB));
                sb.append(plusPrefix).append(strB);
            }
            else if (lenA == lenB) {
                sb.append("2").append(strA.substring(1, lenA));
            }
            else {
                plusPrefix = strB.substring(0, (lenB - lenA));
                sb.append(plusPrefix).append(strA);
            }
        }
        else {
            sb.append("1").append(strA.substring(1, lenA)).append(strB.substring(1, lenB));
        }   

        System.out.print(sb);
    }
}