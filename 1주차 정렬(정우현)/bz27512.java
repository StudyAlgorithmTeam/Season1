package dkfrhflwma;
import java.util.Random;

public class bz27512 {
	private static void quickSort(int[] arr) {
		quickSort(arr,0,arr.length-1);
	}
	private static void quickSort(int[] arr,int start, int end) {
		int part2=partition(arr,start,end);
		if(start<part2-1) {
			quickSort(arr,start,part2-1);
		}
		if(part2<end) {
			quickSort(arr,part2,end);
		}
	}
	private static int partition(int[] arr, int start, int end) {
		int pivot = arr[(start+end)/2];
		while(start<=end) {
			while(arr[start]<pivot)
				start++;
			while(arr[end]>pivot)
				end--;
			if(start<=end) {
				swap(arr,start,end);
				start++;
				end--;
			}
		}
		return start;
	}
	private static void swap(int[] arr,int start,int end) {
		int temp = arr[start];
		arr[start] = arr[end];
		arr[end] = temp;
	}
	
	public static void main(String[] args) {
		Random random = new Random();
		int rand_N = random.nextInt(100)+1;
		int[] randarr = new int[rand_N];
		
		for(int i=0; i<rand_N;i++) {
			randarr[i] = random.nextInt(1000)+1;
			for(int j=0; j<i; j++) {
				if(randarr[j] == randarr[i]) {
					i--;
				}
			}
		}
		
		for(int i=0; i<rand_N; i++) {
			System.out.println(randarr[i]);
		}
		System.out.print("\n");
		//퀘속 정렬
		quickSort(randarr);
		for(int i =0; i<rand_N; i++) {
			System.out.println(randarr[i]);
		}
	}

}
