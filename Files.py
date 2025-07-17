# 'r' : used for open for reading
# 'w' : open for writing
# 'x' : create a new file and open it for writing
# 'a' : open for writing, appending to the end of the file if it existss
# 'b' : for binary mode (image, video...)
# 't' : text mode (default)
# '+' : open a disk file for updating (reading and writing)


# qtn1
# with open("practise.txt", 'r') as f:
#     # data = f.write("hello, My name Zuned Khan.\n")
#     # data2 = f.write("I am a Full Stack Devloper.")

#     data = f.read();

# new_data = data.replace("Full", "Mern");
# print(new_data)

# with open("practise.txt", 'w'):            
#     f.write(new_data)

# count = 0;
# with open("practise.txt", 'r') as f:
#     data = f.read();
#     print(data);
    # num = ""
    # for i in range(len(data)):
    #     if(data[i] == ","):
    #         print(int(num));
    #         num = ""
    #     else:
    #         num += data[i];
           
           # OR

#     num = data.split(",");
#     for val in num:
#         if(int(val) % 2 == 0):
#             count += 1;
# print(count)



# word = "Family";
# with open("practise.txt", 'r') as f:
#     data = f.read();
#     if(data.find(word) != -1):
#         print("found", data)
#     else:
#         print("not found")



         #🟢 Deleting a file

# using os module (import os) : for install : pip install "modules"
# import os

# os.remove(filename)

         #🟢 with Syntex

# with open("demo.txt", 'r') as f: # no need f.close()
#     data = f.read()
#     print(data)



         #🟢 Writing ta aa file 

# f = open("demo.txt", 'w+') # w+ use for all delete
# print(f.read())
# f.write("Hyyyy")
# f.close()

# f = open("demo.txt", 'a') # w is use for overwrite but a use for add something
# f.write("\nI am a Mern Stack Devloper also")
# f.close()

# f = open("demo.txt", 'w') # w is use for overwrite but a use for add something
# f.write("I am a Mern Stack Devloper also")
# f.close()


         # 🟢 Read to a file 

# f = open("demo.txt", 'r+') # r+ usse for overwrite first word
# f.write("Hyyyy")
# print(f.read())
# f.close()


# f = open("demo.txt", "rt") # r : reading and t : text
# data = f.read()
# print(data)
# print(type(data))
# f.close() # best prectise

# f = open("demo.txt", "rt") # r : reading and t : text
# # data = f.read(6)
# line = f.readline()
# line2 = f.readline()
# print(line)
# print(line2)
# f.close() # best prectise