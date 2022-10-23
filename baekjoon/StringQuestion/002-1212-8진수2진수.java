import java.util.Scanner;


public class Main {
    public String getOctToBin(String octStr) throws Exception {
        StringBuilder sb = new StringBuilder();

        char[] octChar = octStr.toCharArray();
        String binBy8 = "";

        String[] firstBinBy8 = {"0", "1", "10", "11", "100", "101", "110", "111"};
        int k = Character.getNumericValue(octChar[0]);
        sb.append(firstBinBy8[k]);

        String[] restBinBy8 = {"000", "001", "010", "011", "100", "101", "110", "111"};
        for (int i = 1; i < octChar.length; i++) {
            k = Character.getNumericValue(octChar[i]);
            sb.append(restBinBy8[k]);
        }
        
        return sb.toString();
    }

    public void solution() throws Exception {
        Scanner sc = new Scanner(System.in);
        System.out.print(getOctToBin(sc.next()));
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}