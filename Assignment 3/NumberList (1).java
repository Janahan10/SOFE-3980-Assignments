import java.lang.Math;

public class NumberList {
	private int smallest = Integer.MAX_VALUE;
	private int largest = Integer.MIN_VALUE;

	public NumberList(){
		this.smallest = smallest;
		this.largest = largest;
	}
	public void addValue(int x){
		this.largest = Math.max(this.largest, x);
		this.smallest = Math.max(this.smallest, x);
	}
	
	public int getLargest(){
		return this.largest;
	}
	public int getSmallest(){
		return this.smallest;
	}
}
