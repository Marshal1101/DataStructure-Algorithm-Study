// https://www.acmicpc.net/source/38774035

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		String N = st.nextToken();
		int B = Integer.parseInt(st.nextToken());
		int value = 0;
		int k = 1;

		for (int i = 1; i < N.length(); i++) {
			k *= B;
		}

		for (int i = 0; i < N.length(); i++) {
			if (N.charAt(i) >= '0' && N.charAt(i) <= '9') {
				value = value + k * (N.charAt(i) - '0');
			} else if (N.charAt(i) >= 'A' && N.charAt(i) <= 'Z') {
				value = value + k * (N.charAt(i) - 55);
			}
			k /= B;
		}
		System.out.println(value);
	}
}