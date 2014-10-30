def skews(text):
    res = [0]
    for s in text:
        if s == 'G':
            k = res[-1] + 1
        elif s == 'C':
            k = res[-1] - 1
        else:
            k = res[-1]
        res.append(k)
    return res

def max_skews_indices(text):
    sk = skews(text)
    m = max(sk)
    print m
    res = []
    for i, p in enumerate(sk):
        if p == m:
            res.append(i)
    return res

def min_skews_indices(text):
    sk = skews(text)
    m = min(sk)
    res = []
    for i, p in enumerate(sk):
        if p == m:
            res.append(i)
    return res



if __name__ == "__main__":
    for s in max_skews_indices("GATACACTTCCCAGTAGGTACTG"):
        print s,