import lq
from datetime import datetime 

def test_push():
    a = []
    assert [1] == lq.push(a,1)

def test_pop():
    a = []
    b = [1, 2, 3, 4,  5]
    assert None == lq.pop(a)
    assert 5 == lq.pop(b)

def test_enque():
    a = []
    b = [1,2,3,4]
    assert [1] == lq.enque(a,1)
    assert [0,1,2,3,4] ==lq.enque(b,0) 

def test_deque():
    a = []
    b = [1,2,3,4]
    assert None == lq.deque(a)
    assert 1 ==lq.deque(b)

def measure_time_stack(a):
    start = datetime.now()
    lq.push(a,5)
    lq.pop(a)
    end  = datetime.now()
    delta  = end - start
    return delta

def measure_time_queue(a):
    start = datetime.now()
    lq.enqueue(a,5)
    lq.dequeue(a)
    end  = datetime.now()
    delta  = end - start
    return delta

def test_time_stack():
    a = [1,2,3,4]
    b = list(range(10000000))
    b.append(1)
    b.pop()
    ta = measure_time_stack(a)
    tb = measure_time_stack(b)
    print (f"Stack | Time A : {ta} | Time B: {tb}")

def test_time_queue():
    a = [1,2,3,4]
    b = list(range(10000000))
    ta = measure_time_queue(a)
    tb = measure_time_queue(b)
    print (f"Queue | Time A : {ta} | Time B: {tb}")