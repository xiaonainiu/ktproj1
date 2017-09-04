import ngram
tokens = open("sample.txt","r")
predicted = 0
response = 0
response_correct = 0
for line in tokens:
	word,condition,answer = line.split()
	if condition == 'OOV':
		string = word
		f = open("dict.txt","r")
		best_val = 0
		best_str_list = []
		for line in f:
			val = ngram.NGram.compare(string,line.strip(),N=2)
			if val > best_val:
				best_val = val
				best_str_list = [line.strip()]
			elif val == best_val:
				best_str_list.append(line.strip())
		if answer in best_str_list:
			response+=1
			response_correct+=1
			predicted = predicted + len(best_str_list)
		else:
			response+=1
			predicted = predicted + len(best_str_list)
		print(string,'->',best_str_list,' value: ', best_val,' success: ',answer in best_str_list)
	else:
		continue
accuracy = float(response_correct)/float(response)
precision = float(response_correct)/float(predicted)
print 'Finish with accuracy: ' ,accuracy
print 'Finish with precision: ' ,precision