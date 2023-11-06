package dkfrhflwma;
import java.util.Random;

public class bz27502 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Random random = new Random();
		int rand_N = random.nextInt(100)+1;
		int[] randarr = new int[rand_N];
		for(int i=0; i<rand_N; i++) {
			randarr[i] = random.nextInt(1000)+1;
			for(int j=0; j<i; j++) {
				if(randarr[i] == randarr[j]) {
					i--;//중복값이 발견되면 i값 초기화
				}
			}
		}
		for(int i=0; i<rand_N;i++) {
			System.out.println(randarr[i]);
		}
		System.out.print("\n");
		
		//선태정렬
		int i,j,least;
		for(i=0;i<rand_N;i++) {
			least = i;
			for(j=i+1; j<rand_N; j++) {
				if(randarr[j]<randarr[least]) {
					least = j;
				}
			}
			if(randarr[i] != least) {//swap의 과정
				int temp = randarr[i];
				randarr[i] = randarr[least];
				randarr[least] = temp;
			}
		}
		for(int z=0; z<rand_N;z++) {
			System.out.println(randarr[z]);
		}
	}

}
