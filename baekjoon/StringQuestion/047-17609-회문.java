import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;

public class Main {
    public int palinedrome(String input) throws Exception {
        int lp = 0;
        int rp = input.length() - 1;
        int tlp, trp;
        Boolean isClean = true;
        while (lp < rp) {
            if (input.charAt(lp) != input.charAt(rp)) {
                if (input.charAt(lp+1) == input.charAt(rp)) {
                    tlp = lp + 1;
                    trp = rp;
                    while (tlp < trp) {
                        if (input.charAt(tlp) != input.charAt(trp)) {
                            isClean = false;
                            break;
                        }
                        tlp++;
                        trp--;
                    }
                    if (isClean) return 1;
                }

                isClean = true;
                if (input.charAt(lp) == input.charAt(rp-1)) {
                    tlp = lp;
                    trp = rp - 1;
                    while (tlp < trp) {
                        if (input.charAt(tlp) != input.charAt(trp)) {
                            isClean = false;
                            break;
                        }
                        tlp++;
                        trp--;
                    }
                    if (isClean) return 1;
                }
                
                return 2;
            }

            lp++;
            rp--;
        }

        return 0;
    }


    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());
        for (int i = 0; i < T; i++) {
            sb.append(palinedrome(br.readLine())).append('\n');
        }

        bw.write(sb.toString());
        bw.flush();
    }


    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}