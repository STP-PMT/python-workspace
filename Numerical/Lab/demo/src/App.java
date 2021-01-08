class App {
    public static void main(String[] args) {
        int[] x = { 1, 2, 3, 4, 5 };
        prefixAverage(x, 5);
    }

    public static void prefixAverage(int[] x, int n) {
        int[] A = new int[n];
        int count1 = 0, count2 = 0;
        for (int i = 0; i <= n - 1; i++) {
            count1++;
            int s = x[0];
            for (int j = 1; j <= i; j++) {
                count2++;
                s = s + x[j];
            }
            A[i] = s / (i + 1);
        }
        System.out.println("count1 " + count1);
        System.out.println("count2 " + count2);
        for (int i = 0; i <= n - 1; i++) {
            System.err.println(A[i]);
        }
    }
}