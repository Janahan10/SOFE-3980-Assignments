package assignment;

import java.util.Scanner;

public class NumberListTester {
	public static void main (String[]args){
		Scanner input = new Scanner(System.in);

		int SEQLENGTH = 4;
		NumberList myNumber = new NumberList();

		for (int i = 0; i < SEQLENGTH; i++) {
			System.out.print("Enter value #" + i + ": ");
			int value = input.nextInt();
			myNumber.addValue(value);
		}
		
		System.out.println("Smallest value = " + myNumber.getSmallest());
		System.out.println("Largest value = " + myNumber.getLargest());

	}
}
