import java.io.IOException;
import java.util.StringTokenizer;
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T= Integer.parseInt(br.readLine());
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		for(int i=0;i<T;i++) {
			st = new StringTokenizer(br.readLine());
			int n1 = Integer.parseInt(st.nextToken());
			int n2 = Integer.parseInt(st.nextToken());
			sb.append(LCM(n1,n2)).append("\n");
		}
		System.out.print(sb);
	}
	
	static int LCM(int n1, int n2) {
		return n1*n2/GCD(n1,n2);
	}
	
	static int GCD(int n1, int n2) {
		if(n2==0) {
			return n1;
		}
		return GCD(n2, n1%n2);
	}
}
