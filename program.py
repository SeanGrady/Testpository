f = open('phy3.txt', 'r')
lines = f.readlines()

header = lines[0].strip().split('\t')

data = []					#There's probably a way to not have to do this, but if I don't make an empty list first it grumbles at me. Help.

for line in lines:
	data.append(line.strip().split('\t'))

nameindex = header.index("Sample Name")		#find which column in the file is the sample name

class Sample:
	
	def __init__(self, samplename):		#because classes
		self.samplename = samplename
	
	def __str__(self):			#for the printings
		return self.samplename

samples = []					#more empty lists because I am the best at programming
names = []

for line in data:				# for all the rows, if the sample name hasn't been seen before, make a Sample object with that name
	if line[nameindex] not in names:
		names.append(line[nameindex])
		samples.append(Sample(line[nameindex]))

for sample in samples:
	print sample
