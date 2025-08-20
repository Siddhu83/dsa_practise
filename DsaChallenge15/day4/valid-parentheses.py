def isValid(self, s: str) -> bool:
    openB = '([{'
    closeB = ')]}'
    my = []
    for i in s:
        if i in openB:
            my.append(i)
        elif i in closeB and closeB.find(i) == openB.find(my[-1]):
            if not my:
                return False
            my.pop()
    return True if len(my) == 0 else False
