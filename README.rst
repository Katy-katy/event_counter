event_counter: Python3 module for counting the events in a short time interval
==============================================================================

Counter can be used for keeping truck of events for
the last 5 minutes (300 seconds) and counting the number
of events in given time interval (the interval must be
from the last 5 munutes).
We assume that we will have no more than 1 mullion events per second.

Installation
------------

The package we can install using pip from the project root:

pip install ./dist/event_counter-0.0.1.tar.gz

Example
-------

**Import Counter:** ::

    from  event_counter.counter import Counter

**Create a Counter:** ::

    my_counter = Counter()

**Every time when an event has happened:** ::

    my_counter.add_event()

**When we need to find the number of events in a time interval:** ::

    events_number = my_counter.count_events("21.05.2018 20:44:02", "21.05.2018 20:47:02")

**Count events that heppened in the last 5 munutes:** ::

    events_number_5_min = my_counter.count_events()

