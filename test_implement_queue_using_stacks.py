from implement_queue_using_stacks import MyQueue

def test_ex1():
    myQueue = MyQueue()
    myQueue.push(1)
    myQueue.push(2)
    assert myQueue.peek() == 1
    assert myQueue.pop() == 1
    assert not myQueue.empty()
 
