/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */
class ListNode {
    val: number;
    next: ListNode | null;
    constructor (val?: number, next?: ListNode | null) {
        this.val = (val === undefined ? 0 : val);
        this.next = (next === undefined ? null : next);
    }
}
function removeNthFromEnd(head: ListNode | null, n: number): ListNode | null {
     let fast = head,
    delayedSteps = 0;

  while (fast && fast.next !== null && delayedSteps < n) {
    fast = fast.next;
    delayedSteps++;
  }
  if (delayedSteps === 0) {
    // means that we have one node and will be removed
    // if it pass this cond we have 1 or more
    return null;
  }
  if (delayedSteps === n - 1) {
    return head!.next;
  }
  let slow = head;
  while (fast && fast.next !== null) {
    fast = fast.next;
    slow = slow!.next;
  }
  if (slow?.next) {
    slow.next = slow.next.next;
  }
  return head;
};