class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
                #[4, 1, 0 7]
                #1: 4 -> 6    1 -> 3.   0 -> 1  7 -> 8
                #2: 6 -> 8.   3 - > 5.   1 -> 2. 8 -> 9
                #3: 8 -> 10.  5 -> 7.    2 -> 3.  9 -> 10
                #4 and 7 become a fleet bc they meet at position 10
                #1 and 0 never become a fleet because they dont catch up to the cars ahead of them
                
                #[4, 2] [1, 2] [0, 1] [7, 1]
                #[7, 1] [4, 2] [1, 2] [0, 1]
                #. 3.    3.     4.5.   10
                #[8, 1] [6, 2] [3, 2] [1, 1]
                cars = []
                for i in range(len(position)):
                    cars.append([position[i], speed[i]])
                
                cars.sort(key=lambda x: x[0], reverse=True)
                stack = []
                for p, s in cars:
                    stack.append((target - p) / s)
                    if len(stack) > 1 and stack[-1] <= stack[-2]:
                        stack.pop()
                return(len(stack))
