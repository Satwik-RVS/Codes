import java.util.*;
public class Hello {

    public static void main(String[] args) {
		// RVS
		Scanner input = new Scanner(System.in);
		int n = input.nextInt(), m = input.nextInt();
		int arr[] = new int[n];
		for(int i=0;i<n;i++)
		{
		    arr[i] = input.nextInt();
		}
		int sumi = 0;
		for(int i=0;i<n;i++)
		{
		    for(int j=i+1;j<n;j++)
		    {
		        if(arr[i] < arr[j])
		        {
		            int temp = arr[i];
		            arr[i] = arr[j];
		            arr[j] = temp;
		        }
		    }
		    if(i<m)
		    {
		        sumi += arr[i];
		    }
		    else
		    {
		        break;
		    }
		}
		System.out.println(sumi);
	}
}
