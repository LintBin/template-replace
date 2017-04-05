#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

from properties import Properties

def replace(old_all,old_str,new_str):
	i =0;
	index = old_all.find(old_str);

	if index != -1:

		old_all = old_all[:index] + new_str + old_all[index+len(old_str):] 
		i = i+1
		old_all = replace(old_all,old_str,new_str)

	return old_all


if __name__ == "__main__":


	dictProperties = Properties("config/config.properties").getProperties()


	template_file = open("template/manage-template.html", 'r')

	content = "";

	file_name = dictProperties['targetFileName']

	for line in template_file:
		content = content + line


	
	for (key,value) in dictProperties.items():

		replaceStr = "#{" + key + "}"
		content = replace(content,replaceStr,value)

	is_exist = os.path.exists("output")
	if not is_exist:
		os.makedirs("output")
    

	outputFile = open("output/" + file_name, 'w')
	outputFile.write(content)
	outputFile.close()



