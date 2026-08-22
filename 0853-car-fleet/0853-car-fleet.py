class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # sort the position array to get descending order of start positions
        # if a car catches up with a car in front, 
        #   - car behind is faster, car in front is slower
        #   - calculate total time for car to reach target
        #   - if total time > slowest time => the car does not intersect => car fleet += 1
        #   - else: car intersects => joins front car car fleet
        # when car intersects => slowest time for car fleet of first car is the car in front 
        fleet_count = 0
        slowest_time = 0
        cars = sorted(zip(position, speed), reverse=True)

        for pos, s in cars:
            time_to_target = (target - pos) / s

            if time_to_target > slowest_time:
                fleet_count += 1
                slowest_time = time_to_target

        return fleet_count