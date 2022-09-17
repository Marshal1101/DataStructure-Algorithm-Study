class Main {

    public static void main(String[] args) throws Exception {
        int T = read();
        StringBuilder sb = new StringBuilder();
        while (T-- > 0) {
            int a = read();
            int b = read();
            int lcm = a * b / gcd(a, b);
            sb.append(lcm).append('\n');
        }
        System.out.print(sb);
    }

    static int gcd(int a, int b) {
        while (b > 0) {
            int r = a % b;
            a = b;
            b = r;
        }
        return a;
    }

    static int read() throws Exception {
        int c, n = System.in.read() & 15;
        while ((c = System.in.read()) > 32) n = (n << 3) + (n << 1) + (c & 15);
        return n;
    }
}