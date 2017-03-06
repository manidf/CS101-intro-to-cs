
# Given the variables defined here, write Python
# code that prints out the distance, in meters,
# that light travels in one processor cycle.

# speed_of_light in meters per second
# cycles_per_second is 2.7 GHz

speed_of_light = 299792458.0 # meters per second
cycle_per_second = 2700000000.0 # processor speed 2.7Ghz

#meters = speed_of_light / cycle_per_second
cycle_distance = speed_of_light / cycle_per_second

print cycle_distance

cycle_per_second = 2800000000.0 # upgraded our processor 2.8Ghz
cycle_distance = speed_of_light / cycle_per_second

print cycle_distance