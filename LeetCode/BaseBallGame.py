#LeetCode Q-682

class solution:
    def baseBall(self,ops:List[str])-> int:
        stack =[]

        for op in ops:
            if op == "+":
               stack.append(stack[-1]+stack[-2])

            elif op == "D":
                stack.append(stack[-1]*2)

            elif op == "C":
                stack.pop()

            else:
                stack.append(int(op))

        return int(sum(stack))