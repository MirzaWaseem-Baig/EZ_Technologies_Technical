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
	    int target=ob.nextInt();
	    seqsearch(a,target);
	    
	}
	public static void seqsearch(int[] a,int target)
	{
	    for(int i=0;i<a.length;i++)
	    {
	        if(a[i]==target)
	        {
	            System.out.println("Available");
	            return;
	        }
	    }
	    System.out.println("UnAvailable");
	}
}
