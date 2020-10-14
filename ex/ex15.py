from sys import argv

script, filename = argv

# open file to read
#  It doesn't return the content os file 
# It makes "file object" which can be used to read/write in file
txt = open(filename)

print(f"Here is your file {filename}")
print(txt.read())
txt.close()

