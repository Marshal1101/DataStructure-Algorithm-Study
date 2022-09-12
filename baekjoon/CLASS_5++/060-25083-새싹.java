public class Main {

    public void solution() throws Exception {
        String s = "         ,r'\"7\n" + 	// \", \n 이 제어문자다.
                    "r`-_   ,'  ,/\n" + 		// \n 이 제어문자다.
                    " \\. \". L_r'\n" + 		// \\, \", \n 이 제어문자다.
                    "   `~\\/\n" + 			// \\, \n 이 제어문자다.
                    "      |\n" + 			// \n 이 제어문자다.
                    "      |";
    
        System.out.print(s);
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}