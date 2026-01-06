public class IsSubTree {
  static class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int x) {
      val = x;
    }
  }

  public boolean isSubTree(TreeNode s, TreeNode t) {
    if (s == null) {
      return false;
    }

    return isSameTree(s.left, t) || isSameTree(s.right, t);
  }

  public boolean isSameTree(TreeNode p, TreeNode q) {
    if (p == null && q == null) {
      return true;
    }

    if (p == null || q == null || p.val != q.val) {
      return false;
    }

    return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
  }

  public static void main(String[] args) {
    IsSubTree solution = new IsSubTree();
    TreeNode s = new TreeNode(3);
    s.left = new TreeNode(4);
    s.right = new TreeNode(5);
    s.left.left = new TreeNode(1);
    s.left.right = new TreeNode(2);
    // s.left.right.left = new TreeNode(0);

    TreeNode t = new TreeNode(4);
    t.left = new TreeNode(1);
    t.right = new TreeNode(2);

    boolean result = solution.isSubTree(s, t);
    System.out.println("Is t a subtree of s? " + result); // Output: false
  }
}
