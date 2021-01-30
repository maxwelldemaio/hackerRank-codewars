/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} node
 * @return {void} Do not return anything, modify node in-place instead.
 */
var deleteNode = function(node) {
    // Steal next node's value
    node.val = node.next.val;
    // Steal the next node's pointer
    node.next = node.next.next;
    return;
};


