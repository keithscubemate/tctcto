r = range
cr = lambda b: [b[i*3:(i+1)*3] for i in r(3)]
leq = lambda ri, t=False: [t:=t|(len(set(r))==1*r[0]!=' ') for r in ri][-1]
w = lambda b: leq(cr(bd)+[bd[i::3] for i in r(3)]+b[::4]+b[2:7:2])
d = lambda b: all(s!=' ' for s in b) and not w(b)
pl = lambda t: "OX"[t%2]
pr = lambda b: '\n'.join(str(r) for r in cr(b))

bd,t=[' ']*9,0
while (n := input("\n{}\nEnter move for {}\n".format(pr(bd),pl(t:=t+1)))):
    if (m := int(n)) in [i for i,s in enumerate(bd) if s==' ']:
        bd[m]=pl(t)
        if w(bd)|d(bd):
            break;

print(pr(bd)+"\n"+"draw" if d(bd) else pl(t)+" wins!")
