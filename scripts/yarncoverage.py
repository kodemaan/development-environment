import sys
import os
fileName = ''
testName = ''
command = 'yarn coverage'
for num, value in enumerate(sys.argv):
  if num == 0:
    continue
  if num == 1:
    fileName = value
    continue
  if testName == '':
    testName = value
  else:
    testName += ' ' + value
  
if fileName != '':
  command += ' ' + fileName + '-test'
if testName != '':
  command += ' -t \'' + testName + '\''
os.system(command)