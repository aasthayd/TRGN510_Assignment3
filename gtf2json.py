#!/usr/bin/python
import sys
import json

#Taking the file path as an argument.
gene_file_path = sys.argv[1]

# Reading the genome file and storing a file content in a variable.
with open (gene_file_path) as gene_file:
    data = gene_file.read() #Read the gene file and saving in variable "data".
data = data.split("\n") #spliting the data at enter(newline).

data_sheet = []
for row in data:
    data_sheet.append(row.split("\t")) #spliting every row of data into columns and storing in data_sheet

gene_data = []
for row in data_sheet:
    if len(row)>2 and row[2] == "gene": #only takes the row which has more than 2 columns and has gene in 3rd column.
        gene_data.append(row)
        
useful_data = []
for row in gene_data:
    gene_dictionary = {} #make a dictionary to store the filtered data.
    gene_dictionary['chr'] = row[0]
    gene_dictionary['startPos'] = row[3]
    gene_dictionary['endPos'] = row[4]
    gene_dictionary['geneName'] = row[8].split(';')[1].split('gene_name')[-1].strip(' ""') #splits the data of column 9 at every ";" then take the gene_name (second column of the seperated data) and split the entry on gene_name to get the gene_name value and removes(strips) the space and "". 
    useful_data.append(gene_dictionary) #the gene_dictionary are added to useful_data. 

print(json.dumps(useful_data))
# prints the data in json format. 






