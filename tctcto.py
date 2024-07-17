r = range
def cr(b): return [b[i*3:(i+1)*3] for i in r(3)]
def cc(b): return [b[i::3] for i in r(3)]
def cd(b): return [[b[0], b[4], b[8]], [b[2], b[4], b[6]]]
def leq(ri, t=False): return [t:=t or (len(set(r))==1 and r[0]!=' ') for r in ri][-1]
def pl(t): return "OX"[t%2]
def pr(b): [print(r) for r in cr(b)]

bd, t = [' '] * 9, 0

pr(bd)
while (n := input()):
    m = int(n)
    if m in [i for i,s in enumerate(bd) if s == ' ']:
        bd[m] = pl(t)
        pr(bd)
        if leq(cr(bd) + cc(bd) + cd(bd)):
            break;
        t+=1

print(pl(t) + " wins!")
