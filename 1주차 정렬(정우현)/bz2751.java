package dkfrhflwma;
import java.util.Arrays;
import java.util.Random;

public class bz2751 {

    public static void sort(int[] arr) {
        if (arr.length < 2) return;

        int mid = arr.length / 2;
        int[] low_arr = Arrays.copyOfRange(arr, 0, mid);
        //배열 복사 0부터 mid까지
        int[] high_arr = Arrays.copyOfRange(arr, mid, arr.length);
        //배열 복사 mid부터 끝까지
        sort(low_arr);
        sort(high_arr);
        
        int m = 0, l = 0, h = 0;
        while (l < low_arr.length && h < high_arr.length) {
            if (low_arr[l] < high_arr[h])
                arr[m++] = low_arr[l++];
            else
                arr[m++] = high_arr[h++];
        }
        while (l < low_arr.length) {
            arr[m++] = low_arr[l++];
        }
        while (h < high_arr.length) {
            arr[m++] = high_arr[h++];
        }
    }

    public static void main(String[] args) {
        Random random = new Random();
        int rand_N = random.nextInt(100) + 1;
        int[] randarr = new int[rand_N];

        for (int i = 0; i < rand_N; i++) {
            randarr[i] = random.nextInt(1000) + 1;
            for(int j=0; j<i; j++) {
            	if(randarr[j] == randarr[i]) {
            		i--;
            	}
            }
        }

        for (int i = 0; i < rand_N; i++) {
            System.out.println(randarr[i]);
        }
        System.out.print("\n");

        sort(randarr); 

        for (int i = 0; i < rand_N; i++) {
            System.out.println(randarr[i]);
        }
    }
}
