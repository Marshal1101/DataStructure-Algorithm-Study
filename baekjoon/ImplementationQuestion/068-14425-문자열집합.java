import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.util.StringTokenizer;
import java.util.HashMap;

public class Main {
    int N, M, i;
    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        
        HashMap<String, String> map = new HashMap<>();
        for (i = 0; i < N; i++) {
            map.put(br.readLine(), "yes");
        }
        
        int count = 0;
        
        for (i = 0; i < M; i++) {
            if (map.get(br.readLine()) != null) count++; 
        }

        System.out.println(count);
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}