import ngram

tokens = open("labelled-tokens.txt","r")
response = 0
response_correct = 0
for line in tokens:
	word,condition,answer = line.split()
	if condition == 'OOV':
		string = word
		f = open("dict.txt","r")
		best_val = 9999999999999
		best_str = ""
		for line in f:
			
			val = ngram.NGram.compare(string,line.strip(),N=2)
			if val < best_val:
				best_val = val
				best_str = line.strip()
		if best_str == answer:
			response+=1
			response_correct+=1
		else:
			response+=1
		print(best_str, best_val,best_str==answer)
	else:
		continue
accuracy = response_correct/response
print ("Finish with accuracy: " +accuracy)