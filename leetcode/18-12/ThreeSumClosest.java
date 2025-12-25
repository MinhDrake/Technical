public class ThreeSumClosest {
  // similar to threeSum
  public int threeSumClosest(int[] nums, int target) {
    int result = Integer.MAX_VALUE;

    // ele - 2 , ele -1 still be candidate
    for (int i = 0; i < nums.length - 2; i++) {
      if (i > 0 && nums[i] == nums[i - 1]) {
        continue;
      }

      int sum = target - nums[i];

      for (int j = i + 1; j < nums.length; j++) {
        int currSum = nums[j] + nums[j+1];
        if (Math.abs(currSum - sum) < result) {
          result = nums[i] + nums[j] + nums[j+1]
        }
      }
    }

    return result;
  }
}
