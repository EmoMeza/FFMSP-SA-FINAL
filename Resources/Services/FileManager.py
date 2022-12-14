import os
import Resources.Classes.Sequences as seq


def open_File_By_Name(name):
    current_path=os.getcwd() 
    file_path=current_path+"/Resources/Examples/"+str(name)
    file=open(file_path,"r")
    sequences=[]
    for line in file:
        sequence=seq.Sequences(line)
        sequences.append(sequence)
    file.close()
    return sequences

def get_Input_From_File(number,stage):
    if(stage==0):
        name="100-300-0"
    if(stage==1):
        name="100-600-0"
    if(stage==2):
        name="100-800-0"
    if(stage==3):
        name="200-300-0"
    if(stage==4):
        name="200-600-0"
    if(stage==5):
        name="200-800-0"
    current_path=os.getcwd() 
    if(number<10):
        filename=name+"0"+str(number)+".txt"
    elif(number==10):
        filename=name+"10.txt"
    file_path=current_path+"/Resources/Examples/"+str(filename)
    file=open(file_path,"r")
    sequences=[]
    for line in file:
        sequence=seq.Sequences(line)
        sequences.append(sequence)
    file.close()
    return sequences