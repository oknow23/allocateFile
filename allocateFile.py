import os
import re

VERSION = '0.1.0'
DBG = 0

# Allocate dictionary
dic1={'name':'HTML','path':'D:\OneDrive - 台州北校\Transfer\Buy','reg':'.htm','type':'file'}
dic2={'name':'Movie','path':'D:\[Movie]','reg':'\.\d\d\d\d\.','type':'folder'}
dic3={'name':'Apen','path':'D:\\apen','reg':'[a-zA-Z].*?[0-9]+','type':'folder'}
fileList=[dic1,dic2,dic3]

print('Allocate to folder '+VERSION+': start')
print("---------------------------------------")
# list file
for fileNames in os.listdir(os.getcwd()):
	# check have dictionary in file list?
	for dic in fileList:
		try:
			# check file name and type
			if re.search(dic['reg'],fileNames).group() and not ((os.path.isdir(fileNames)) ^ (dic['type'] == 'folder')):
				print(dic['name']+':')
				print(' '+fileNames)

				# move file
				if not os.path.isdir(dic['path']):
					os.makedirs(dic['path'])
				os.rename(fileNames,dic['path']+'\\'+fileNames)
		except:
			test="test"
print("---------------------------------------")

print('Done!!')

if DBG == 0:
	os.system("pause")