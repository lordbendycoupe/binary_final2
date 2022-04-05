##########################################################
# common binary strand search                           #
# by: tim sellers                                       #
# timsellers888@protonmail.com                          #
##########################################################
import numpy as np
import pandas as pd
import os
import sys

## main idea ##
# basically this program just opens binary files, stores their content in a dataframe, matches strings and uses index to calcuate offset
#i chose pandas dataframes due to their matrix like behavior, we can conceptualize mathematically a way to find the common strings and offse
# for every file n, there exists a 1-d dataframes data[k].....data[j] for j,k <= n
# therefore, there exists a data[i] such that i ɛ data[k] ∩ data[j] ... data[h]
#assuming this is true, we can point to each element that is in the intersection between 2 or more dataframes, and their index is the offset


path = os.getcwd()
file_list = os.listdir()
file_storage = list()
exclude = set(['New folder', 'Windows', 'Desktop', 'env', '.git', 'README.md', 'requirements.txt']) 

while True:
   
    try:
        if len(file_list) >= 3: #2+ binaries & *.py
            for path, dirs, files in os.walk(path, topdown=True):
                for filename in file_list:
                    dirs[:] = [d for d in dirs if d not in exclude]
                    fullpath = os.path.join(path, filename)
                    if not filename.endswith('.py'):
                        if not filename in exclude:
                            files = [i for i in exclude if os.path.isfile(i)]
                            with open(os.path.join(filename), 'rb') as f:
                                data = pd.DataFrame(f, columns=['bytes'])
                                file_storage.append(filename)
                                length = data['bytes'].str.len()
                                argmax = np.where(length == length.max())[0]
                                key = data.loc[argmax]
                                argo = key.to_numpy().ravel().tolist()         
                                for col in key.columns: 
                                    flag = 0
                                    index = 0
                                for line in f:  
                                    index += 1 
                                    if key in line:
                                        flag +=1
                                    break     
                                if flag == 0:
                                    print('longest common string in: ', 
                                    filename,
                                    '\n',
                                    key, 
                                    '\n',
                                    'string length: ', 
                                    sys.getsizeof(argo))
                                else: 
                                    None                    
    except ValueError:
            print("needs at least 2 files in project directory (/binary)")
    break 

# all common elements

try:

    def strand_analysis(data):       
        for common in enumerate(data):
            common = data.merge(data, how = 'inner')
            
        print('\n',
        'common strands between',
         (len(file_storage)), 
         'files', 
         '\n', 
         file_storage, 
         '\n', 
         common)

except: ValueError:  print('no common strands')

else:  strand_analysis(data)



