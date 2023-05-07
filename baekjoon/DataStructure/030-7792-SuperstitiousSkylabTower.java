import java.util.*;

public class Super {
  long[][] dp = new long[13][10];

  boolean valid(int a, int b) {
    return !(a == 1 && b == 3) && b != 4;
  }

  long f(int n, int p) {
    if ( dp[n][p] != -1 ) return dp[n][p];
    long ret = 0;
    for ( int i = 0; i < 10; i++ )
      if ( valid(p, i) ) ret += f(n - 1, i);
    return dp[n][p] = ret;
  }

  void solve() {
    for (long[] m : dp) Arrays.fill(m,-1);
    for ( int i = 0; i < 10; i++ ) dp[0][i] = 1;

    Scanner scan = new Scanner(System.in);
    int T = scan.nextInt();
    while ( T-- > 0 ) {
      long k, h, ans = 0;
      k = scan.nextLong();
      h = scan.nextLong();
      for ( int n = 1; k != 0; n++ ) {
        int t = (int)(k % 10); k /= 10;
        for ( int i = 0; i < t; i++ )
          if ( valid((int)(k % 10), i) ) ans += f(n - 1, i);
      }
      System.out.println(ans * h);
    }
  }

  public static void main(String[] args){
    new Super().solve();
  }
}