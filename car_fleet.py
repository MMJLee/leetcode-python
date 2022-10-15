# https://leetcode.com/problems/car-fleet/
from typing import List


class CarFleet:
    def car_fleet(self, target: int, pos: List[int], speed: List[int]) -> int:
        # get time for each car to reach target, sorted by position
        time = [float(target - p) / s for p,
                s in sorted(zip(pos, speed), key=lambda x: x[0])]
        fleets, cur = 0, 0
        # if time takes longer than current, it is a new fleet so change cur time to it and increment fleet counter
        for t in time[::-1]:
            if t > cur:
                fleets += 1
                cur = t
        return fleets
