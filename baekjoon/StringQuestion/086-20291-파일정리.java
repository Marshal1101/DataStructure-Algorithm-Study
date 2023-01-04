import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.TreeMap;
import java.util.Map;

public class Main {
    public void solution() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Map<String,Integer> map = new TreeMap<String,Integer>();
        int N = Integer.parseInt(br.readLine());
        
        
        int cnt, idx;
        String filename, ext;
        for (int i = 0; i < N; i++) {
            filename = br.readLine();
            idx = filename.indexOf(".");
            ext = filename.substring(idx+1);
            cnt = map.getOrDefault(ext, 0);
            map.put(ext, cnt+1);
        }

        for (Map.Entry<String,Integer> entry : map.entrySet()) {
            System.out.println(entry.getKey() +" "+ entry.getValue());
        }
    }

    public static void main(String[] args) throws IOException {
        new Main().solution();
    }
}