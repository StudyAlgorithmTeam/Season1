package dkfrhflwma;
import java.util.Scanner;


public class bz2750 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int rand_N = sc.nextInt();
		int[] randarr = new int[rand_N];
		
		for(int i=0; i<rand_N; i++) {
			randarr[i] = sc.nextInt();
		}
		
		System.out.print("\n");
		//삽입 정렬
		int i,j,key;
		for(i = 1; i < rand_N; i++) {
			key = randarr[i];
			for(j = i-1; j>=0 && randarr[j]>key; j--) {
				randarr[j+1] = randarr[j];//j값을 오른쪽으로 이동 시킴
			}
			randarr[j+1] = key; // key값을 다시 위치에 넣어 준다
		}
		
		for(int z = 0; z < rand_N; z++) {
			System.out.println(randarr[z]);
        }
		
	}

}
