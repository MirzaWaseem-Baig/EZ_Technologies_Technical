import java.util.*;
public class Main
{
	public static void main(String[] args) {
		Scanner ob=new Scanner(System.in);
		int n=ob.nextInt();
		System.out.println(add(n));
	}
	public static int add(int n)
	{
	    if(n<=0)
	    {
	        return 0;
	    }
	    return n+add(n-1);
	}
}
