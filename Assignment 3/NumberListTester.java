
public class NumberListTester {
	public static void main (String[]args){
		NumberList myNumber = new NumberList();
		myNumber.addValue(1);
		myNumber.addValue(100000);
		
		System.out.println("Smallest value = " + myNumber.getSmallest()):
		System.out.println("Largest value = " + myNumber.getLargest())
		;
	}
}
