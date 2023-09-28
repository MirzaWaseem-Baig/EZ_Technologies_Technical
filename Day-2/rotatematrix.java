import java.util.*;
public class Main
{
	public static void main(String[] args) {
		Scanner ob=new Scanner(System.in);
		int r=ob.nextInt();
		int c=ob.nextInt();
		int[][] arr=new int[r][c];
		int[][] arr1=new int[c][r];
		for(int i=0;i<r;i++)
		{
		    for(int j=0;j<c;j++)
		    {
		        arr[i][j]=ob.nextInt();
		    }
		}
		for(int i=0;i<r;i++)
		{
		    for(int j=0;j<c;j++)
		    {
		        System.out.print(arr[i][j]+" ");
		    }
		    System.out.println();
		}
		for(int i=0;i<r;i++)
		{
		    for(int j=0;j<c;j++)
		    {
		        arr1[i][j]=arr[j][i];
		    }
		}
		for(int i=0;i<r;i++)
		{
		    int k=c-1;
		    for(int j=0;j<c;j++)
		    {
		        if(k==-1)
		        {
		            break;
		        }
		        else{
		            arr[i][j]=arr1[i][k];
		            k--;
		        }
		        
		    }
		}
		for(int i=0;i<r;i++)
		{
		    for(int j=0;j<c;j++)
		    {
		        System.out.print(arr[i][j]+" ");
		    }
		    System.out.println();
		}
	}
}
