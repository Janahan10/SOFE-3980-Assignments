import java.util.Scanner;

public class NumberListTester {
	public static void main (String[]args){
		Scanner input = new Scanner(System.in)
		NumberList myNumber = new NumberList();

		for (int i = 0; i < 4; i++) {
			System.out.println('Enter a number: ');
			int val = input.nextInt();
			myNumber.addValue(val);
		}
		
		System.out.println("Smallest value = " + myNumber.getSmallest());
		System.out.println("Largest value = " + myNumber.getLargest());
	}
}
