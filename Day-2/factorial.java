import java.util.*;
public class Main
{
	public static void main(String[] args) {
		Scanner ob=new Scanner(System.in);
		int n=ob.nextInt();
		System.out.println(fact(n));
	}
	public static int fact(int n)
	{
	    if(n==1)
	    {
	        return 1;
	    }
	    return n*fact(n-1);
	}
}
