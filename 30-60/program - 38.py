def sol(prb, pmb, pr):
    prob_sep_travel = (prb * (1 - pmb)) + (pmb * (1 - prb))
    prob_rom = prob_sep_travel * pr
    return prob_rom

a = float(input())
b = float(input())
c = float(input())
d = sol(a, b, c)
print("%.6f"%d)