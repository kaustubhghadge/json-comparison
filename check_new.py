import json
import os

def compare_json_files(folder_path):
    # list to store all json files in the folder
    json_files = [f for f in os.listdir(folder_path) if f.endswith('.json')]
    
    # list to store all the extracted data from the files
    data_list = []
    
    # loop through all the files and extract their data
    for file in json_files:
        file_path = os.path.join(folder_path, file)
        
        with open(file_path) as f:
            data = json.load(f)
        
        data_list.append((file, data))
        
    # compare the data from all files
    result = []
    for i in range(len(data_list)):
        file1, data1 = data_list[i]
        
        for j in range(i+1, len(data_list)):
            file2, data2 = data_list[j]
            
            for d1 in data1:
                d2 = next((d for d in data2 if d['title'] == d1['title']), None)
                
                if d2 is None:
                    result.append("\"" + d1['title'] + "\" is present in \"" + file1 + "\", but missing from \"" + file2 + "\"")
                else:
                    for key in d1.keys():
                        if key not in d2 or d1[key] != d2[key]:
                            result.append("\"" + key + "\" is different in \"" + file1 + "\" and \"" + file2 + "\"")
                
    # write the result to the output.txt file
    with open(os.path.join(folder_path, 'output.txt'), 'w') as f:
        f.write("\n".join(result))
        
    print("Data comparison complete. Output file generated: output.txt")

# example usage
compare_json_files('./compare_files')
