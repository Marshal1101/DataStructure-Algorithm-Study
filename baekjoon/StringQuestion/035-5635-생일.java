import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Comparator;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        ArrayList<Integer> birthList = new ArrayList<>();
        HashMap<Integer, String> map = new HashMap<>();

        int N = Integer.parseInt(br.readLine());
        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String name = st.nextToken();
            String day = String.format("%02d", Integer.parseInt(st.nextToken()));
            String month = String.format("%02d", Integer.parseInt(st.nextToken()));
            String year = st.nextToken();
            int birth = Integer.parseInt(year + month + day);
            birthList.add(birth);
            map.put(birth, name);
        }
        
        birthList.sort(Comparator.naturalOrder());
        System.out.println(map.get(birthList.get(birthList.size()-1)));
        System.out.print(map.get(birthList.get(0)));
    }
}