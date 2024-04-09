#Q-374 Guess Number Higher or Lower
def guessName(self,n:int)->int:
    l,r = 1,n

    while True:
        m=(l+r)//2
        res = guess(m)
        if res > 0:
            l = m + 1
        elif res < 0:
             r = m
        else:
             return m