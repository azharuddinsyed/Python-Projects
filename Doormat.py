def doormat(a,b):
    d = int(b/a) # to store quotient of b/a
    s = '.|.'  # special character to be displayed
    w = 'WELCOME'
    m = 0 # to store the values incremented by 3
    idx = 0 # index of list l  (Actual list of odd numbers)
    idx1 = 0 # index of list lx (reversal of list l)
    l = [p for p in range(1,a) if p%2 != 0] # to create list of odd numbers from range 1 to 7
    lx = l[::-1] # to reverse list l
    for x in range(a):
        if x != (int(a/2)) and not(x > int(a/2)):
            s = s*l[idx]
            print(s.center(b, '-'))
            s = '.|.'
            idx += 1
        elif x == (int(a/2)):
            print(w.center(b, '-'))
            m -= d
        else:
            s = s*lx[idx1]
            print(s.center(b, '-'))
            s = '.|.'
            idx1 = idx1 + 1


doormat(7, 21)