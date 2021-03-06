import java.util.Arrays;

public class quickSort {
	public static void quicksorting(int[] arr,int low,int high) {
		if (low>high) {
			return;
		}
		int mid=low+((high-low)/2);
		int i=low;
		int j=high;
		int pivot=arr[mid];
		while(i<=j) {
			while(arr[i]<pivot) {
				i++;
			}
			while(arr[j]>pivot) {
				j--;
			}
			if(i<=j) {
				int temp=arr[i];
				arr[i]=arr[j];
				arr[j]=temp;
				i++;
				j--;
			}

		}
		if(low<j) {
			quicksorting(arr,low,j);
		}
		if (i<high) {
			quicksorting(arr,i,high);
		}
		
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println("program to implement quick sort algorithm");
		int[] arr= {9,8,7,6,5};
		System.out.println("before sorting ...");
		System.out.println(Arrays.toString(arr));
		quicksorting(arr,0,arr.length-1);
		System.out.println("after sorting ...");
		System.out.println(Arrays.toString(arr));
	}

}
