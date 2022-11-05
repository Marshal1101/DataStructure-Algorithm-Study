/** https://www.acmicpc.net/source/39290346 */

import java.util.*;
import java.io.*;

public class Main {
	static int[] powNumbers = {1, 2, 4};
	
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String binary = br.readLine();
		char[] binaryCharArray = binary.toCharArray();
		int len = binaryCharArray.length;
		int index;
		
		if(len % 3 != 0) //2진수 -> 8진수 # 3bit씩 끊어서 계산
			index = len / 3;
		else 
			index = (len / 3) - 1;
		
		char[] octalCharArray = new char[index + 1];
		
		int powNumber = 0, num = 0; 
		
		while(--len >= 0) {
			num += (binaryCharArray[len] - '0') * powNumbers[powNumber];
			//끝에서부터 2진수를 8진수로 변환
			
			if(powNumber == 2) {
				octalCharArray[index] = (char) (num + '0');
				index--;
				powNumber = 0;
				num = 0;
			} else powNumber++;
		}
		
		if(index == 0) //len % 3 != 0 일 때 발생
			octalCharArray[index] = (char) (num + '0');
		
		System.out.println(octalCharArray);
	}
}
