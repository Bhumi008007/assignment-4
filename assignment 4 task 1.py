try:
     file1 = open('sample file.txt','r')
     reading_file = file1.read()
     print(reading_file)
     file1.close()
except FileNotFoundError:
     print("file not found")