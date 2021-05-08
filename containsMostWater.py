class Solution:
    def maxArea(self, height: List[int]) -> int:
        # two pointers
        left = 0
        right = len(height)-1
        maxArea = 0
        
        while (left < right):
            # move smaller one
            if height[left] < height[right]:
                maxArea = max(maxArea, (right-left)*(height[left]))
                left += 1
            elif height[right] < height[left]:
                maxArea = max(maxArea, (right-left)*(height[right]))
                right -= 1
            # if they're equal height, move left till it reaches a taller height
            # then move right till it reaches a taller height
            # if left meets right then return
            else:
                maxArea = max(maxArea, (right-left)*(height[right]))
                anchor = height[left]
                while (anchor >= height[left]):
                    left += 1
                    if left == right:
                        return maxArea
                # once a taller height than left is found then calculate new area
                maxArea = max(maxArea, (right-left)*(height[right]))
                anchor = height[right]    
                while (anchor >= height[right]):
                    right -= 1
                    if left == right:
                        return maxArea
        return maxArea