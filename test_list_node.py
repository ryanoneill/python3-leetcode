from list_node import ListNode, to_list, from_list

def test_ex1():
    items = [1,2,3,4,5]
    head = from_list(items)
    assert head is not None
    result = to_list(head)
    assert result == items
