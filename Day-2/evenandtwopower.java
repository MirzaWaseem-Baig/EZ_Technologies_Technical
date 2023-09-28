import java.util.*;
public class Main
{
	public static void main(String[] args) {
		Scanner ob=new Scanner(System.in);
		int r1=ob.nextInt();
		int r2=ob.nextInt();
		int n=ob.nextInt();
		int[] arr=new int[n];
		int i=0;
		while(i<n)
		{
		    int c=ob.nextInt();
		    if(r1<=c&&r2>=c){
		    arr[i]=c;
		    i++;
		    }
		}
		for(int j=0;j<n;j++)
		{
		    if(arr[j]%2==0)
		    {
		        System.out.print(arr[j]+" ");
		    }
		}
		int k=0;
		for(int j=0;j<n;j++)
		{
		    if(arr[j]==Math.pow(2,k))
		    {
		        System.out.print(arr[j]+" ");
		    }
		    k++;
    	}
	}
}
