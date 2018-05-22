from event_counter.counter import Counter
import time


def test_counter():
    my_counter = Counter()

    # test 1: add max allowed number of events
    # (should take less than 300 seconds
    t0=time.time()
    time_0 = time.strftime("%d.%m.%Y %H:%M:%S", time.localtime())

    for i in range(300):
        for k in range(1000000): # 1 mullion events per 1 sec
            my_counter.add_event()
    time_1 = time.strftime("%d.%m.%Y %H:%M:%S", time.localtime())
    print("Adding 300 000 000 events took ",time.time()-t0)

    # test 2: count all 300 000 000 events
    t0=time.time()
    result = my_counter.count_events(time_0, time_1)
    t1 = time.time()
    print("Calculating of", result, "events took ", t1-t0)

    # test 3: count events from a specified time up to now
    time_2 = time.strftime("%d.%m.%Y %H:%M:%S", time.localtime())
    time.sleep(1)

    for i in range(100):
        my_counter.add_event()
    print("from", time_1, "up to now we have ", my_counter.count_events(time_2))

    # test 4: count events for the last 5 minutes (default setting):
    print("In the last 5 minutes we had", my_counter.count_events())