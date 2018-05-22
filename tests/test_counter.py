from event_counter.counter import Counter
import time

my_counter = Counter()

# test 1: count all events in Counter.events_by_seconds
def test_counter1():

    for i in range(300):
        my_counter.add_event()
    time.sleep(1)
    result = my_counter.count_events()
    assert result==300

# test 2: count events in an time interval
def test_counter2():

    time.sleep(1)
    time_1 = time.strftime("%d.%m.%Y %H:%M:%S", time.localtime())
    time.sleep(1)
    for i in range(5):
        my_counter.add_event()
    time.sleep(1)
    time_2 = time.strftime("%d.%m.%Y %H:%M:%S", time.localtime())
    result = my_counter.count_events(time_1, time_2)
    assert result==5

# test 3: add max number of events
def test_counter3():
    t0=time.time()
    for i in range(300):
        for k in range(1000000): # 1 mullion events per 1 sec
            my_counter.add_event()
    result=time.time()-t0
    print("Adding 300 000 000 events took ",time.time()-t0)

# test 4: count all events for last 5 minutes (should take no more than 1 sec)
def test_counter4():
    time.sleep(1)
    t0=time.time()
    result = my_counter.count_events()
    t1 = time.time()-t0
    print("Counting of ", result, "events took", t1)
    assert t1<1


