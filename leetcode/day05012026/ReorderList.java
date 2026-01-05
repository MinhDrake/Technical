import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.List;

public class ReorderList {
  static class ListNode {
    int val;
    ListNode next;

    ListNode(int x) {
      val = x;
      next = null;
    }
  }

  // Using List
  public void reorderListArrayList(ListNode head) {
    if (head.next == null) {
      return;
    }

    List<ListNode> nodes = new ArrayList<>();
    ListNode current = head;
    while (current != null) {
      nodes.add(current);
      current = current.next;
    }

    int left = 0, right = nodes.size() - 1;
    // break left == right for case even length (stop at right)
    while (left < right) {
      nodes.get(left).next = nodes.get(right);
      left++;
      // prevent circular preference
      if (left == right) {
        break;
      }
      nodes.get(right).next = nodes.get(left);
      right--;
    }

    nodes.get(left).next = null; // terminate the list
  }

  // Using deque
  public void reorderList(ListNode head) {
    Deque<ListNode> deque = new ArrayDeque<>();
    ListNode current = head;
    while (current != null) {
      deque.add(current);
      current = current.next;
    }

    ListNode dummy = new ListNode(0);
    ListNode newHead = dummy;

    while (!deque.isEmpty()) {
      newHead.next = deque.pollFirst();
      newHead = newHead.next;

      if (!deque.isEmpty()) {
        newHead.next = deque.pollLast();
        newHead = newHead.next;
      }
    }

    newHead.next = null;
    head = dummy.next;
  }

  public static void main(String[] args) {
    ListNode head = new ListNode(1);
    head.next = new ListNode(2);
    head.next.next = new ListNode(3);
    head.next.next.next = new ListNode(4);
    head.next.next.next.next = new ListNode(5);

    ReorderList solution = new ReorderList();
    solution.reorderList(head);

    ListNode current = head;
    while (current != null) {
      System.out.print(current.val + " ");
      current = current.next;
    }

    // even list
    ListNode head2 = new ListNode(1);
    head2.next = new ListNode(2);
    head2.next.next = new ListNode(3);
    head2.next.next.next = new ListNode(4);
    solution.reorderList(head2);
    current = head2;
    System.out.println();
    while (current != null) {
      System.out.print(current.val + " ");
      current = current.next;
    }
  }
}
