import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {
    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int month = Integer.parseInt(st.nextToken());
        int day = Integer.parseInt(st.nextToken());
        int idxDay, temp = 0;

        String[] firstWeek = {"SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"};
        int[] monthDays = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

        for (int i = 1; i < month; i++) {
            temp += monthDays[i];
        }
        temp += day;
        idxDay = temp % 7;

        bw.write(firstWeek[idxDay]);
        bw.flush();
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}