import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.util.StringTokenizer;
import java.util.HashSet;


public class Main {
    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());

        HashSet<Integer> setA = new HashSet<>();
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < a; i++) {
            setA.add(Integer.parseInt(st.nextToken()));
        }

        HashSet<Integer> setB = new HashSet<>();
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < b; i++) {
            setB.add(Integer.parseInt(st.nextToken()));
        }

        HashSet<Integer> sub1 = new HashSet<>(setA);
        HashSet<Integer> sub2 = new HashSet<>(setB);
        sub1.removeAll(setB);
        sub2.removeAll(setA);
        sub1.addAll(sub2);
        
        System.out.println(sub1.size());
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}
