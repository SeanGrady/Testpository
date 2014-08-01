f = open('phy3.txt', 'r')
lines = f.readlines()
header = lines[0].strip().split('\t')
print header
