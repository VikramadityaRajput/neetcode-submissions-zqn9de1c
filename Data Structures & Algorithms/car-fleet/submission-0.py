class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_to_speed = {}
        for i in range(len(position)):
            pos_to_speed[position[i]] = speed[i]
        pos_sort = sorted(position)
        pos_sort = pos_sort[::-1]
        cars = []
        for j in range(len(position)):
            ps = [pos_sort[j], pos_to_speed[pos_sort[j]]]
            cars.append(ps)
        #I have now created a list of descending position values and their speeds.
        stack = []
        for pos, speed in cars:
            time = (target - pos) / speed
            if len(stack) == 0  or time > stack[-1]: #empty stack edge case for start
                stack.append(time) #if a car gets there before then its part of the fleet, so no need to add
        return len(stack)



        
        