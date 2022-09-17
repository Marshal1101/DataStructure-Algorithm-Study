import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {
	static int n,m;
	static boolean[] ba; 
	static int[] ia;
	static StringBuilder sb = new StringBuilder();
	
	public static void main(String[] args) throws IOException {
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	StringTokenizer st = new StringTokenizer(br.readLine());
	
	n = Integer.parseInt(st.nextToken());
	m = Integer.parseInt(st.nextToken());
	
	ba = new boolean[n+1];
	ia = new int[n+1];
	
	backTracking(0);
	
	bw.write(sb.toString());
	bw.flush();
	}
	
	static void backTracking(int i) {
		if(i==m) {
			for(int j=0;j<m;j++) sb.append(ia[j]).append(" ");
			sb.append("\n");
			return;
		}
		
		for(int j=1;j<=n;j++) {
			if(ba[j]) continue;
			ba[j] = true;
			ia[i] = j;
			backTracking(i+1);
			ba[j] = false;
		}
	}
}