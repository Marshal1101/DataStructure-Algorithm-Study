import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] s = br.readLine().split(" ");
		int[] compare = {1,1,2,2,2,8};
		String[] answer = new String[6];
				
		for(int i=0; i < s.length; i++) {
			int piss = Integer.parseInt(s[i]);
			
			if(piss == compare[i]) answer[i] = "0";
			else answer[i] = Integer.toString(compare[i] - piss);
		}
		
		System.out.print(String.join(" ", answer));
	}

}
