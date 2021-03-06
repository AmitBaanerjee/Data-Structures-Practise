/*Given a binary matrix A, we want to flip the image horizontally, then invert it, and return the resulting image.

To flip an image horizontally means that each row of the image is reversed.  For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].

To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0. For example, inverting [0, 1, 1] results in [1, 0, 0].

Example 1:

Input: [[1,1,0],[1,0,1],[0,0,0]]
Output: [[1,0,0],[0,1,0],[1,1,1]]
Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]
Example 2:

Input: [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
Explanation: First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]].
Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
 * 
 */
import java.util.Arrays;
public class FlippingImage {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int [][] inputImage= {{1,1,0},{1,0,1},{0,0,0}};
		for (int i=0;i<inputImage.length;i++) {
			int length=inputImage[i].length;
			for (int j=0;j<length/2;j++) {
				int temp=inputImage[i][j];
				inputImage[i][j]=inputImage[i][length-1-j];
				inputImage[i][length-1-j]=temp;
				
			}
		}
		for (int i=0;i<inputImage.length;i++) {
			for(int j=0;j<inputImage[i].length;j++) {
				int value=inputImage[i][j];
				if(value==1) {
					value=0;
				}
				else if(value==0){
					value=1;
				}
				inputImage[i][j]=value;
			}
		}
		
		System.out.println("Reversed Image is :-");
		for (int i=0;i<inputImage.length;i++) {
			for(int j=0;j<inputImage[i].length;j++) {
				System.out.print(inputImage[i][j]+"\t");
			}
			System.out.println("\n");
		}
		
		

	}

}
