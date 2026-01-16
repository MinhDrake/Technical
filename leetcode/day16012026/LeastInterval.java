// https://neetcode.io/problems/task-scheduling/question?list=neetcode150
public class LeastInterval {
  // Call fmax is the most frequent task in the list
  // we have all (fmax-1) group of tasks and the (n+1) length ( 1 for element fmax
  // and n for the cycle)
  // and max_count (the number of elements have same length as max)
  // the total = (fmax-1)*(n+1) + max_count
  // In case fmax only exist in n+1 group and not up to max_count -> max here is
  // len of array cause the solution equal the
  // len off array
  // c
  public int leastInterval1(char[] tasks, int n) {
    // find max-count and the fmax
    int[] counter = new int[26];
    int fMax = 0;
    int maxCount = 0;

    for (int i = 0; i < tasks.length; i++) {
      int currentIdx = tasks[i] - 'A';
      counter[currentIdx]++;
      if (counter[currentIdx] > fMax) {
        fMax = counter[currentIdx];
        maxCount = 1;
      } else if (counter[currentIdx] == fMax) {
        maxCount += 1;
      }
    }

    return Math.max(tasks.length, (fMax - 1) * (n + 1) + maxCount);
  }

  // above is about math calculation
  // if we want to count the real things, use the priorityHeap to take elements
  // from the most frequently to the least one
  publicint leastInterval(char[] tasks, int n) {
    Map<Character, 
  }

  public static void main(String[] args) {
    LeastInterval obj = new LeastInterval();
    char[] tasks = new char[] { 'X', 'X', 'Y', 'Y' };
    System.out.println(obj.leastInterval(tasks, 2));
  }
}
