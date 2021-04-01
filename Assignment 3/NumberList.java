package assignment;

import java.lang.Math;
import java.util.Collections;
import java.util.PriorityQueue;

public class NumberList {
	private int SEQLENGTH = 4;

	private PriorityQueue<Integer> minHeap;
	private PriorityQueue<Integer> maxHeap;

	public NumberList(){
		this.minHeap = new PriorityQueue<Integer>();
		this.maxHeap = new PriorityQueue<Integer>(Collections.reverseOrder());
	}

	public void addValue(int x){
		this.minHeap.add(x);
		this.maxHeap.add(x);
	}

	public int getLargest() {
		return this.maxHeap.peek();
	}

	public int getSmallest() {
		return this.minHeap.peek();
	}
}
