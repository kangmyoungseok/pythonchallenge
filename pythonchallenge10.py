# http://www.pythonchallenge.com/pc/return/bull.html
def A005150(n):
    p = "1"

    seq = [1]

    while (n > 1):

        q = ''

        idx = 0 # Index

        l = len(p) # Length

        while idx < l:

            start = idx

            idx = idx + 1

            while idx < l and p[idx] == p[start]:

                idx = idx + 1

            q = q + str(idx-start) + p[start]

        n, p = n - 1, q

        seq.append(int(p))

    return seq
A005150(5)[-1]
len(str(A005150(31)[-1]))