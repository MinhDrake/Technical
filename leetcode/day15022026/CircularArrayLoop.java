package day15022026;

import java.util.HashSet;
import java.util.Set;

// https://leetcode.com/problems/circular-array-loop/?envType=problem-list-v2&envId=two-pointers
public class CircularArrayLoop {
  // /Intuition/ Hint:
  // The cycle in this problem is special and you must consider these things
  // before deep dive into solution:

  // Cycle must has length >= 2 ( ex: -1,-2,-,3-,4,-5, self-loop end at last
  // element) -> Think about something like set / array curr_path
  // All the arrows in the loop "must" point in one direction. (it must be all
  // forward , or all backwrard) -> at each position, rememeber the first sign of
  // that element and check at every step before return result
  // Note: In case you want to module for negatvie number, please use
  // next_pos = ((i+nums[i])%n+n)%n
  // DFS find cycle
  public boolean circularArrayLoop(int[] nums) {
    if (nums == null || nums.length == 1) {
      return false;
    }
    boolean[] visited = new boolean[nums.length];
    for (int i = 0; i < nums.length; i++) {
      if (visited[i]) {
        continue;
      }
      int current = i;
      Set<Integer> currPath = new HashSet<>();
      int sign = nums[i] > 0 ? 1 : -1;
      while (true) {
        visited[current] = true;
        currPath.add(current);
        // module for both pos and neg
        int nextPos = ((current + nums[current]) % nums.length + nums.length) % nums.length;
        if (sign * nums[nextPos] < 0 || current == nextPos) {
          break;
        }

        if (currPath.contains(nextPos)) {
          // check length >= 2 -> this is the point, currPath has visited
          if (currPath.size() > 1) {
            // print the path
            System.out.println(currPath);
            return true;
          }
          // self-loop
          break;
        }

        if (visited[nextPos]) {
          break;
        }

        current = nextPos;
      }
    }

    return false;
  }

  public boolean circularArrayLoopUsingTwoPointers(int[] nums) {
    for (int i = 0; i < nums.length; i++) {
      int slow = i;
      int fast = getNext(nums, slow);
      boolean isForward = nums[i] > 0;
      while (isSameDirection(nums[getNext(nums, fast)], isForward)
          && isSameDirection(nums[getNext(nums, getNext(nums, fast))], isForward)) {
        if (slow == fast) {
          // is same possition
          if (slow == getNext(nums, slow)) {
            break;
          }

          return true;
        }
        slow = getNext(nums, slow);
        fast = getNext(nums, getNext(nums, fast));
      }

      nums[slow] = 0;
    }

    return false;
  }

  // this method has two missions: stop the loop when visited (= 0), and check is
  // same direction
  public boolean isSameDirection(int val, boolean lastDirection) {
    if (val == 0)
      return false;
    return (val > 0) == lastDirection;
  }

  public int getNext(int[] nums, int idx) {
    return (((idx + nums[idx]) % nums.length) + nums.length) % nums.length;
  }

  public static void main(String[] args) {
    CircularArrayLoop sol = new CircularArrayLoop();
    // System.out.println(sol.circularArrayLoop(new int[] { 2, -1, 1, 2, 2 })); //
    // true
    // System.out.println(sol.circularArrayLoop(new int[] { 1, 1, 1, 1, 1 })); //
    // true
    // System.out.println(sol.circularArrayLoop(new int[] { -1, -2, -3, -4, -5, 6
    // })); // false
    // System.out.println(sol.circularArrayLoop(new int[] { 1, -1, 5, 1, 4 })); //
    // true
    // System.out.println(sol.circularArrayLoop(new int[] { -1, -2, -3, -4, -5 }));
    // // false

    System.out.println(sol.circularArrayLoopUsingTwoPointers(new int[] { 2, -1, 1, 2, 2 }));
    System.out.println(sol.circularArrayLoopUsingTwoPointers(new int[] { 1, 1, 1, 1, 1 })); // true
    System.out.println(sol.circularArrayLoopUsingTwoPointers(new int[] { -1, -2, -3, -4, -5, 6
    })); // false
    System.out.println(sol.circularArrayLoopUsingTwoPointers(new int[] { 1, -1, 5, 1, 4 })); // true
    System.out.println(sol.circularArrayLoopUsingTwoPointers(new int[] { -1, -2, -3, -4, -5 })); // false

  }
}
