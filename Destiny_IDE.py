"""
Created on Wed Jan 12 21:15:16 2022

@author: Fahim Ferdous
"""

import os
import subprocess


file_name = input("<File name> ")

content_list = []
for i in open(file_name,"r").readlines():
  content_list.append(i.replace("\n",""))

def print_file():
   for line,i in enumerate(content_list):
    if line>=9:
      print(" "+str(line+1)+"|"+str(i))
              
    elif line<9:
      print("  "+str(line+1)+"|"+str(i))

class IDE():
  def __init__(self,file_name):
    self.file_name = file_name
    self.flag = False
    self.Flgs = []
    self.mistakes = 0
    self.current_line = 1
    self.help = {"!gt":"Go to a certian line to edit it",
                 "!s":"Save the edited file",
                 "!nl":"Creates a new line",
                 "!q":"Quit the ide",
                 "!e":"Edit the current line",
                 "./":"Run current the file",
                 "!cp":"Paste current line to another line",
                 "!c -o":"Clears the output",
                 "!help":"get help"}
    
  def run(self):
    global content_list
    def ui(self):
  
        print("================["+str(self.file_name)+"]================")
        if self.flag == False:
          print_file()
          print("\n")
          for i in self.Flgs:
            print(i)
          
        else:
          print(self.flag)
          print("\n")
          for i in self.Flgs:
            print(i)
        
        print("\n")
        command = input("["+str(self.current_line)+":"+str(len(content_list))+"]")
        
        
        if "!gt" in command:
          try:
            line_number = int(command.replace("!gt",""))-1
            current_line_copy = line_number+1
            
            if current_line_copy>len(content_list):
              pass
            elif current_line_copy<=0:
              pass
            
            else:
              self.current_line = line_number+1
            
            
            try:
              i = content_list[self.current_line]
              if self.current_line>=9:
                print(" "+str(self.current_line+1)+"|"+str(i))
                
              elif self.current_line<9:
                print("  "+str(self.current_line+1)+"|"+str(i))
                
            except IndexError:
              pass
            
          except ValueError:
            self.Flgs.append("["+str(self.mistakes)+"]: not a valid line number")
            self.mistakes += 1
        
        elif "!e" in command:
          ledit = input("<edit on line `"+str(self.current_line)+"`>")
          if ledit == ":!c":
            pass
          else:
            content_list[self.current_line-1] = ledit
            
        elif "!nl" in command:
          content_list.append("")
            
        elif "!help" in command:
          for i in self.help:
            if i == " : ":
              pass
            else:
              self.Flgs.append(str(i)+" : "+self.help[i])
        
        elif "!c -o" in command:
          del self.Flgs[:]
        
        elif "!s" in command:
          with open(file_name,"w") as FILE:
            for i in content_list:
              FILE.write(i+"\n")

        elif "!q" in command:
            return "Status.break"
            
        
        elif "./" in command:
            command = "python3 "+str(file_name)
            process = subprocess.Popen(command,stdout=subprocess.PIPE, stderr=subprocess.PIPE,shell=True)
            output_result, error = process.communicate()
            
            self.Flgs.append(output_result.decode("utf-8"))
        
        elif "!cp" in command:
          copy = command.replace("!cp","")
          paste = self.current_line
          content_list[int(copy)-1] = content_list[int(paste)-1]
          
        
    while True:
      x = ui(self)
      if x == "Status.break":
          break
      
      os.system("cls")
    

if __name__ == "__main__":
  IDE = IDE(file_name)
  IDE.run()
