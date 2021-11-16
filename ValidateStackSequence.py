class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        my_stack = []
        for num in pushed:
            my_stack.append(num)
            while((my_stack) and (my_stack[-1] == popped[0])):
                my_stack.pop()
                popped.pop(0)
        return False if my_stack else True
