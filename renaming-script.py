# Python3 code to rename multiple  
# files in a directory or folder 
  
# importing os module 
import os 
  
#importing regex
import re 

#Andrew's code
def renameFile(inputFileName):
    return "-".join(re.sub( r"([A-Z])"), r" \1", inputFileName).split()

files = ["FinalExamSchedule", "FinalExam", "2020FallRegistration", "Spring2021Schedule"]
[print(renameFile(i)) for i in files]
#end of Andrew's code

# Function to rename multiple files 

def main():
    for count, filename in enumerate(os.listdir(r"C:\Users\jesus\Documents\Work")):   
        #separateWords = renameFile(filename)
        spacesToDashes = filename.replace(" ", "-")
        underscoreToDashes = filename.replace("_", "-")
        oldFileName = filename  
        # rename() function will 
        # rename all the files 
        #os.rename((os.path.join(r"C:\Users\jesus\Documents\Work", oldFileName)), os.path.join(r"C:\Users\jesus\Documents\Work", separateWords))
        os.rename((os.path.join(r"C:\Users\jesus\Documents\Work", oldFileName)), os.path.join(r"C:\Users\jesus\Documents\Work", spacesToDashes)) 
        os.rename((os.path.join(r"C:\Users\jesus\Documents\Work", oldFileName)), os.path.join(r"C:\Users\jesus\Documents\Work", underscoreToDashes))



# Driver Code 
if __name__ == '__main__': 
    # Calling main() function 
    main()
