import java.lang.Math;

public class NumberList {
	private int count;
	private int sum;
	private int smallest = Integer.MIN_VALUE;
	private int largest = Integer.MAX_VALUE;
	
	public void Data(){
		count = 0;
		sum = 0;
		smallest = 0;
		largest = 0;
	}
	
	public NumberList(int x){
		smallest = Math.min(smallest, x);
		largest = Math.max(largest, x);	
	}
	public void newValue(int x){
		sum = sum + x;
		count++;
		if (x > largest)
			largest = x;
		else if (x < smallest)
			smallest = x;
	}
	
	public int getLargest(){
		return largest;
	}
	public int getSmallest(){
		return smallest;
	}
}
