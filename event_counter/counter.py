from collections import deque
from time import time, mktime, strptime



class Counter(object):
    """Counter can be used for keeping truck of events for
    the last 5 minutes (300 seconds) and counting the number
    of events in given time interval (the interval must be
    from the last 5 munutes).
    We assume that we will have no more than 1 mullion events per second.
    """

    def __init__(self, supported_interval=300):
        self.events_by_seconds = deque(maxlen=supported_interval+5)
        self.events_by_seconds.append([int(time()), 0])
        self.supported_interval = supported_interval


    def add_event(self):
        """Update the number of events in self..events_by_seconds
        for the current second.
        """
        event_time = int(time())

        if self.events_by_seconds[-1][0] == event_time:
            self.events_by_seconds[-1][1] +=1
        else:
            self.events_by_seconds.append([event_time, 1])


    def count_events(self, time_from='', time_to=''):
        """Count how many events happened from time_from (included)
         to time_to (excluded). The precision is one second.

        Parameters
        ----------
        time_from : str, optional
            String in format: "29.08.2017 11:05:02".
            If not provided, start of supported interval will be used.
            For example, if it is "29.08.2017 11:05:02" now,
            "29.08.2017 11:00:02" will be used.
        time_to : str, optional
            String in format: "29.08.2017 11:05:02".
            If not provided, the events will be cound up to
            current second. If it is "29.08.2017 11:05:02" now,
            the events that happened at "29.08.2017 11:05:01" will
            be included, but the events that happened at
            "29.08.2017 11:05:02" will not be included"

        Returns
        -------
        count : int
            number of events in given time interval
        """
        count_from, count_up = self._validate_input(time_from, time_to)

        count = 0
        #assimption: the user more often is interested in newest data
        for i in reversed(self.events_by_seconds):
            if i[0] >= count_up:
                continue
            if i[0] < count_from:
                break
            count+=i[1]
        return count


    def _validate_input(self, time_from, time_to):
        supported_boundary_up = int(time())
        supported_boundary_from = supported_boundary_up-self.supported_interval

        if time_from == '': #default value
            count_from = supported_boundary_from
        else:
            try:
                count_from = mktime(strptime(time_from, "%d.%m.%Y %H:%M:%S"))
            except:
                raise ValueError("time_from does not match format "
                             "\"%d.%m.%Y %H:%M:%S\", got ", time_from)

        if time_to == '':#default value
            count_up = supported_boundary_up
        else:
            try:
                count_up = mktime(strptime(time_to, "%d.%m.%Y %H:%M:%S"))
            except:
                raise ValueError("time_to does not match format "
                             "\"%d.%m.%Y %H:%M:%S\", got ", time_to)

        if count_from > count_up:
            raise ValueError("time_from must be before time_to; got time_from",
                             time_from, "time_to", time_to)

        # we keep truck of events only in supported interval(300 sec)
        if count_from < supported_boundary_from:
            raise ValueError("time_from must be in supported interval (5 minutes)")

        if count_up > supported_boundary_up:
            raise ValueError("time_to must be in supported interval. "
                             "If you want to count events up to now, "
                             "use default value for time_to.")

        return count_from, count_up