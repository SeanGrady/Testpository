import os

data = os.path.join(os.environ['TESTPOSITORY'], 'phy3.txt')
with open(data, 'r') as f:
    header = f.readlines()[0]

print header.strip().split('\t')
