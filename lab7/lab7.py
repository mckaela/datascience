import os

def make_dict(files):
	l = list('`~!@#$%^&*()_+-=[{]}\\|:;\'\",<.>/? \n\t\v0123456789')
	
	dict = {}
	for f in files:
		with open(f,'r') as fp:
			for line in fp.read().split('\n'):
				for word in line.split(' '):
					word = ''.join([w for w in word if w not in l])
					word = word.lower()
					if word=='':
						continue
					val = dict.get(word,-1)
					if val==-1:
						dict[word] = 1
					else:
						dict[word] = val+1
	return dict

def make_vectors(files,words):
	vectors = []
	for file in files:
		temp_dict = make_dict([file])
		vector = []
		for word in words:
			vector += [temp_dict.get(word,0)]
		vectors += [vector]
	return vectors


def main():
	files = os.listdir(os.getcwd())
	eng_files = [f for f in files if f[-1]=='e']
	frn_files = [f for f in files if f[-1]=='f']

	engdict = make_dict(eng_files)
# 	print(len(engdict))
	frndict = make_dict(frn_files)
# 	print(len(frndict))

	import operator
	engdict = sorted(engdict.items(), key=operator.itemgetter(1),reverse=True)
# 	print(eng_dict)
	frndict = sorted(frndict.items(), key=operator.itemgetter(1),reverse=True)
# 	print(eng_dict)

# 	with open('eng','w') as f:
# 		f.write(str(engdict))

# 	with open('frn','w') as f:
# 		f.write(str(frndict))
	
	eng_words,engcounts = zip(*engdict)
	frn_words,frncounts = zip(*frndict)
	
	eng_words_taken = eng_words[500:5500]
	frn_words_taken = frn_words[500:5500]
	eng_vectors = make_vectors(eng_files,eng_words_taken)
	frn_vectors = make_vectors(frn_files,frn_words_taken)
	with open('engvectors','w') as f:
		f.write(str(eng_vectors))

	with open('frnvectors','w') as f:
		f.write(str(frn_vectors))
main()



import matplotlib.pyplot as plt

plt.plot(engcounts,'b*', frncounts,'ro')
plt.yscale('log')
plt.xscale('log')
plt.show()
