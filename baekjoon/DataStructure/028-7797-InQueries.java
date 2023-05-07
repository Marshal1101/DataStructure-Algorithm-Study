import java.util.*;

public class Query {
  int[][] f = new int[120000][6];
  int[][] calc = new int[6][11000];
  boolean[] del = new boolean[120000];

  void solve() {
    Scanner scan = new Scanner(System.in);

    int T = scan.nextInt();
    for ( int tcase = 1; tcase <= T; tcase++ ) {
      System.out.printf( "Case #%d:\n", tcase );

      int a = scan.nextInt();
      int b = scan.nextInt();   
      int x = scan.nextInt();
      int m = scan.nextInt();
      int n = scan.nextInt();

      for ( int[] i : f ) Arrays.fill(i,0);
      for ( int[] i : calc ) Arrays.fill(i,0);
      Arrays.fill(del,false);
      
      a %= m; b %= m; x %= m;

      for ( int r = 0; r <= n; r++ )
        for ( int c = 0; c <= 5; c++ )
          if ( r == 0 || c == 0 ) f[r][c] = 0;
          else {
            f[r][c] = (a * f[r-1][c] + b * f[r][c-1] + x) % m;
            calc[c][f[r][c]]++;
          }
      
      int q = scan.nextInt();
      int r, c, left, right, sum;

      while ( q-- > 0 ) {
        String line = scan.next();
        
        if ( line.equals("insert") ) {
          n++;
          for ( int i = 1; i <= 5; i++ ) {
            f[n][i] = scan.nextInt();
            calc[i][f[n][i]]++;
          }
        }
        else if ( line.equals("remove") ) { 
          r = scan.nextInt();
          if ( r <= n && !del[r] ) {
            del[r] = true;
            for ( int i = 1; i <= 5; i++ ) calc[i][f[r][i]]--;
          }
        }
        else if ( line.equals("max") ) {
          c = scan.nextInt();
          for ( int i = 10000; i >= 0; i-- )
            if ( calc[c][i] != 0 ) { System.out.println(i); break; }
        }
        else if ( line.equals("min") ) {
          c = scan.nextInt();
          for ( int i = 0; i <= 10000; i++ )
            if ( calc[c][i] != 0 ) { System.out.println(i); break; }
        }
        else if ( line.equals("range") ) {
          c = scan.nextInt();
          left = scan.nextInt();
          right = scan.nextInt();
          sum = 0;
          for ( int i = left; i <= right; i++ ) sum += calc[c][i];
          System.out.println(sum);
        }

      }
    }
  }

  public static void main(String[] args) {
    new Query().solve();
  }
}