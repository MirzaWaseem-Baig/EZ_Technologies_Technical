import java.util.*;
public class Main
{
	public static void main(String[] args) {
	    Scanner ob=new Scanner(System.in);
	    int n=ob.nextInt();
		int[] a=new int[n];
		for(int i=0;i<n;i++)
		{
		    a[i]=ob.nextInt();
		}
		sum1(a);
	}
	public static void sum1(int[] a)
	{
	    int sum=0;
		for(int i=0;i<a.length;i++)
		{
		    sum=sum+a[i];
		}
		System.out.print(sum);
	}
	
	
	
}
