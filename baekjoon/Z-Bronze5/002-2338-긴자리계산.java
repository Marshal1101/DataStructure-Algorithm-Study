import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.math.BigInteger;
import java.util.StringTokenizer;

public class Main {
    public static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws Exception {
        BigInteger A = new BigInteger(new StringTokenizer(br.readLine()).nextToken());
        BigInteger B = new BigInteger(new StringTokenizer(br.readLine()).nextToken());

        System.out.println(A.add(B));
        System.out.println(A.subtract(B));
        System.out.println(A.multiply(B));
    }
}