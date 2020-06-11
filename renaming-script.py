# Python3 code to rename multiple  
# files in a directory or folder 
  
# importing os module 
import os 
  
#importing regex
import re 

# Function to rename multiple files 

def main():
    for count, filename in enumerate(os.listdir(r"C:\Users\jesus\Documents\Work")):   
        oldFileName = filename
        filename = "-".join(re.sub(r"([A-Z])", r" \1", str(filename)).split()).replace(" ", "-").replace("_", "-").replace("--", "-")
        # rename() function will 
        # rename all the files 
        print("Old name:\t" + oldFileName)
        print("New name:\t" + filename)
        # os.rename((os.path.join(r"C:\Users\jesus\Documents\Work", oldFileName)), os.path.join(r"C:\Users\jesus\Documents\Work", filename))
        # os.rename((os.path.join(r"C:\Users\jesus\Documents\Work", oldFileName)), os.path.join(r"C:\Users\jesus\Documents\Work", spacesToDashes)) 
        # os.rename((os.path.join(r"C:\Users\jesus\Documents\Work", oldFileName)), os.path.join(r"C:\Users\jesus\Documents\Work", underscoreToDashes))




# # Driver Code 
if __name__ == '__main__':
    # Calling main() function 
    main()
