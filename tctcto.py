r = range
def cr(b): return [b[i*3:(i+1)*3] for i in r(3)]
def cc(b): return [b[i::3] for i in r(3)]
def cd(b): return [b[::4], b[2:7:2]]
def leq(ri, t=False): return [t:=t or (len(set(r))==1 and r[0]!=' ') for r in ri][-1]
def pl(t): return "OX"[t%2]
def pr(b): return '\n'.join(str(r) for r in cr(b))

bd, t = [' '] * 9, 0
while (n := input("\n{}\nEnter move for {}\n".format(pr(bd),pl(t:=t+1)))):
    m = int(n)
    if m in [i for i,s in enumerate(bd) if s == ' ']:
        bd[m] = pl(t)
        if leq(cr(bd) + cc(bd) + cd(bd)):
            break;

print(pl(t) + " wins!")
