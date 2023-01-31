import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {

	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringBuilder sb = new StringBuilder();
	
//	static void input() throws IOException{
//		StringTokenizer st = new StringTokenizer(br.readLine());
//		
//		
//	}
	static boolean visit[] = new boolean[10001];
	
	static void func(int k) {
		
			
		String temp = Integer.toString(k);
		
//		int[] digits = new int[temp.length()];
		
		for (int n = 0; n<temp.length(); n++) {
			k  += temp.charAt(n) - '0';
		}
		
		if (k>=10001) return;
		if (visit[k]) return;
//		System.out.println(k);
		
		visit[k] = true;
		func(k);
	}
	
	
	public static void main(String[] args) {
		
		
		for (int i=0; i<10001; i++) visit[i] = false;
		
		
		for (int i=0; i<10001; i++) {
			if (visit[i]) continue;
			func(i);
		}
		
		for (int i=0; i<=10000; i++) {
			if(!visit[i]) sb.append(i).append("\n");
		}
		
		System.out.println(sb);
	}
	
	
}
