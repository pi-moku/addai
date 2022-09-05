from csv import *

def insert(name,data):
    with open(name, 'a', newline='') as f_object:
            # Pass the CSV  file object to the writer() function
            writer_object = writer(f_object)
            # Result - a writer object
            # Pass the data in the list as an argument into the writerow() function
            writer_object.writerow(data)
            # Close the file object
            f_object.close()


count = 0

for i in range(1000):
    data = [count,count,count+count]
    name = 'main.csv'
    insert(name,data)
    count += 1
