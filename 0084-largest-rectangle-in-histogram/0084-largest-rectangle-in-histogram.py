class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # maxArea = 0
        # n = len(heights)
        # for i in range(n):
        #     minh = float('inf')
        #     for  j in range(i,n):
        #         minh = min(minh,heights[j])
        #         maxArea = max(maxArea,minh*(j-i+1))
        # return maxArea

        n = len(heights)
        leftsmall = [-1] * n      # default: no smaller on left
        rightsmall = [n] * n      # default: no smaller on right
        stack = []

        # next smaller on LEFT
        for i in range(n):
            while stack and heights[i] <= heights[stack[-1]]:
                stack.pop()
            leftsmall[i] = stack[-1] if stack else -1
            stack.append(i)

        stack.clear()

        # next smaller on RIGHT
        for i in range(n - 1, -1, -1):        # must go rightâleft
            while stack and heights[i] <= heights[stack[-1]]:
                stack.pop()
            rightsmall[i] = stack[-1] if stack else n
            stack.append(i)

        maxA = 0
        for i in range(n):
            width = rightsmall[i] - leftsmall[i] - 1
            maxA = max(maxA, heights[i] * width)

        return maxA