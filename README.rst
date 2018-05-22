Event Counter.

The package we can install using pip from the project root.

pip install ./dist/event_counter-0.0.1.tar.gz

from  event_counter.counter import Counter
my_counter = Counter()

my_counter.add_event()

print(my_counter.count_events("21.05.2018 20:44:02", "21.05.2018 20:47:02"))


output:
176