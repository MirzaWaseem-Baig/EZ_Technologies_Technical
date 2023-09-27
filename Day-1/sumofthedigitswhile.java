import java.util.*;
public class Main
{
	public static void main(String[] args) {
		Scanner ob=new Scanner(System.in);
		int n=ob.nextInt();
		int sum=0;
		int last=0;
		while(n>0)
		{
		    last=n%10;
		    sum=sum+last;
		    n=n/10;
		}
		System.out.println(sum);
	}
}
