from scipy.special import comb
L = input()
CUT_NUM = 11
print(comb(int(L) - 1, CUT_NUM, exact=True))
