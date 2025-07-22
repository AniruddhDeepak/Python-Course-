user_input=input("Enter data : ")
user_input1=input("Enter text to write to the file : ")
print("Data successfully written to output.txt")
file1=open("output.txt","w")
data_enter=file1.write(user_input1 + "\n")
file1.close()


user_input2=input("Enter additional text to append : ")
print("Data successfully appended")
file1=open("output.txt","a")
data_append=file1.write(user_input2)
file1.close()


print("Final Contents of output.txt : ")
file1=open("output.txt","r")
data_read=file1.read()
print(data_read)
file1.close()


