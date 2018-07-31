import os
import re

def chose(list , num):
	for x in list:
		if x == num:
			return 0
		else:
			return 1
	return 1
	


files = os.listdir('./model')
model_list = []
for model_file in files:
	temp = re.split("\_|\.",model_file)
	if chose(model_list,temp[3]):
		model_list.append(temp[3])

for x in model_list:
	
	command1 = "python select_rl_no_training.py " + x
	command2 = "python select_plot_results.py " + x
	os.system(command1)
	os.system(command2)
