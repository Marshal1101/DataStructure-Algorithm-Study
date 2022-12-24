public class InsertionSort {
    public staitc void main(String[] args) throws Exception {
        int[] = {};
        int temp;
        for (int i = 1; i < arr.length; i++) {
            for (int j = i; j > 0; j--) {
                if (arr[j] < arr[j-1]) {
                    temp = arr[j];
                    arr[j] = arr[j-1];
                    arr[j-1] = temp;
                }
            }
        }

        for (int i = 0; i < arr.length; i++) {
            System.out.println(arr[i])
        }
    }

    public void s(int[] arr) throws Exception {
        int b = arr.length
        int temp;
        for (i = b/2 - 1; i > 0; i--) {

            func(arr, b, i);
        }

        for (int i = b-1; i >= 0; i--) {
            temp = arr[0];
            arr[0] = arr[i];
            arr[i] = temp;

            func(arr, i, 0)
        }
    }
}