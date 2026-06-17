def find_m(n):
    return [d+n//d or 0 for d in range(2,int(n**0.5)+1) if n % d == 0] or ['1']
print(*[(i,find_m(i)[0]) for i in range(1_500_000,1_500_110+1) if str(find_m(i)[0]).endswith("7") and str(find_m(i)[0]).count('2') == 0],sep='\n')

print(*[(i, m) for i in range(1_500_000, 1_500_111) if str(m := ([d+i//d or 0 for d in range(2, int(i**0.5)+1) if i % d == 0] or ['1'])[0]).endswith("7") and '2' not in str(m)], sep='\n')

