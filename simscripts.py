# This program creates simulated scripts given a template script and scenarios

# Extract all csv data
# csv contains 104 rows and 146 columns
import csv
csvFile = open(r"C:\Users\mengy2\Desktop\simulated scripts\CDFA_v1.1_Simulated_Scenarios - 01_Sample.csv")
csvReader = csv.reader(csvFile)
csvData = list(csvReader)
csvFile.close()

# Extract non-variable data from template
templateFile = open(r"C:\Users\mengy2\Desktop\simulated scripts\CDFA_1.1_sim_template.icl")
templateData = templateFile.readlines()
templateFile.close()
# Header data is from line 1-80, or [0] to [79]
# Footer data si from line 82-830, or [81] to [829]


tempPath = "C:\\Users\\mengy2\\Desktop\\simulated scripts\\"
for i in range(146):#146 total scenarios
    
    tempFile = open(tempPath + csvData[10][i+1],"w")
    for j in range(80):#0-79
        tempFile.write(templateData[j])
    for k in range(10):#0-10
        tempFile.write(csvData[k+39][i+1]+"\n")
    for m in range(81, 830):#81-829
        tempFile.write(templateData[m])
    tempFile.close()
