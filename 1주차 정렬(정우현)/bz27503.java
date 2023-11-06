package dkfrhflwma;
import java.util.Random;


public class bz27503 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Random random = new Random();
		int rand_N = random.nextInt(100)+1;
		int[] randarr = new int[rand_N];
		
		for(int i=0; i<rand_N; i++) {
			randarr[i] = random.nextInt(1000)+1;
			for(int j=0; j<i; j++) {
				if(randarr[i] == randarr[j]) {
					i--;
				}
			}
		}
		
		for(int i=0; i<rand_N; i++) {
			System.out.println(randarr[i]);
		}
		System.out.print("\n");
		
		//버블정렬
		
		int i,j,temp;
		for(i=rand_N-1;i>0;i--) {
			for(j=0; j<i; j++) {
				if(randarr[j]>randarr[j+1]) {
					temp = randarr[j];
					randarr[j] = randarr[j+1];
					randarr[j+1] = temp;
				}
			}
		}
		
		for(int z=0; z<rand_N; z++) {
			System.out.println(randarr[z]);
		}
	}

}
