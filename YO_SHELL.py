# -*- coding: utf-8 -*-
"""
@Program Name: Yo-Shell V1 Starter Code
YO-SHELL Date: Feb 29,2016
@Author:  Azharuddin Mohammad
          SaiChowdary Amaraneni
          Vishnu Chaitanya Mandalapu
          
@Description:- This program will implement a subset of the existing 
bash commands like copy,move,chmod etc that we use

"""

import os
import sys
import shutil
import math
import time

command_history = [] #list to hold all commands

"""
    @Name: runShell
    @Description:
        Loop that drives the shell environment
    @Params: None
    @Returns: None
"""

def runShell():
    while True:
        print("in runshell")
        inp= input('parser-$ ') 
        
        parts = inp.split(" ") 
        command_history.append(parts[0]) #collects history
        
        #print(command_history[:])
        if parts[0] == "cp":
           if len(parts)==3:
              copy(parts[1],parts[2])
           else:     #to detect error
               print("Needs 3 arguments")
        elif parts[0]=="mv":
           if len(parts)==3:
              move(parts[1],parts[2])
           else:
               print("Needs 3 arguments")
        elif parts[0]=="rm":
           if len(parts)==2:
              remove(parts[1])
           else:
               print("Needs 2 arguments")
        elif parts[0]=="cat":
           if len(parts)==2:
              cat(parts[1])
           else:
               print("Needs 2 arguments")
        elif parts[0]=="chmod":
            if len(parts)==3:
               changeModify(parts[1],parts[2])
            else:
               print("Needs 3 arguments")
        elif parts[0]=="cd":
            if len(parts)==2:
               cd(parts[1])
            else :
                print("Needs 2 arguments")
        elif parts[0]=="history":
           if len(parts)==1:
              history() 
           else:
               print("Needs only 1 arguments")
        elif parts[0]=="wc":
            if len(parts) > 1:
                if parts[1]=="-l":
                    wcWithFlag(parts[2]) #passing filename
                else:
                    wc(parts[1]) 
            else:
                print("Needs more than 1 argument")
                
        elif parts[0]=="ls":
            if len(parts)==1:
               dir=os.getcwd()
               ls(dir)
            elif parts[1]== "-l":
               ls(dir)
            elif len(parts) > 1:
                if parts[1] == "-s" or "-a" or "-m" or "-c":
                   lsWithFlag(parts[1])
          
"""
    @Name: ls
    @Description:
        Does a directory listing
    @Params: 
        dir (string) - The directory to be listed
    @Returns: None
"""

def ls(dir):
    os.listdir(" ")
    for r,d,files in os.walk('.'):
        for f in files:
            print(f)
            print("\n")
    
"""
    @Name: wc
    @Description:
        Does wordcount in  a file
    @Params: 
        file (string) - Name of the file that needs the words counted
    @Returns: None
"""

def wc(file):
    numWords=0
    f=open(file)
    for lines in f:
        words=lines.split(" ")
        numWords=numWords+len(words)
    output="Num of words in "+ file + numWords
    print(output)
    
"""
    @Name: wcWithFlag
    @Description:
        Does wordcount and gives num of lines
    @Params: 
        file (string) - Name of the file that needs the words counted and the number of lines
    @Returns: None
"""

def wcWithFlag(file):
    numLines=0
    numWords=0
    f=open(file)
    for lines in f:
        words=lines.split(" ")
        numLines=numLines+1
        numWords=numWords+len(words)
    output="Num of words in "+ file + numWords
    print(output)
    output="Num of lines in "+file + numLines
    print(output)
           
"""
    @Name: copy
    @Description:
        Copies filenames
    @Params: 
        first (string) - Name of the first file
        second (string) - Name of the second file
    @Returns: None
"""
def copy(first,second):
    shutil.copyfile(first,second) 
    print("file name copied ")
    

"""
    @Name: move
    @Description:
        Renames first filename with second
    @Params: 
        first (string) - Name of the first file
        second (string) - Name of the second file
    @Returns: None
"""    
    
def move(first,second):
    os.rename(first,second)
    print("file name renamed")
        
"""
    @Name: remove
    @Description:
        Removes the mentioned file
    @Params: 
        first (string) - Name of the file that needs to be removed
    @Returns: None
"""

def remove(first):
    os.remove(first)
    print("file removed")

"""
    @Name: cat
    @Description:
        Prints the data in the file
    @Params: 
        first (string) - Name of the file that needs to read
    @Returns: None
"""

def cat(first):
    f = open(first,'r')
    print(f.read())

"""
    @Name: changeModify
    @Description:
        Does a directory listing
    @Params: 
        num (integer) - Levels of permission to be set to the file
        second (String) - Name of the file that needs the permission change
    @Returns: None
"""

def changeModify(num,second):
    print("in chmod func")
    permission=int(num)
    os.chmod(second,permission)
    print("changed permission of")
    print(second)
    print("permission") 
    
"""
    @Name: cd
    @Description:
        Does a directory change
    @Params: 
        newDir (string) - Opens the folder specified in the shell.
    @Returns: None
"""

def cd(newDir):
    try:
       os.chdir(newDir) #given directory
    except:
       print("could find the folder entered")
    if newDir[0]=="..":
       os.chdir(os.newDir.oldpwd(newDir)) #previous directory
    elif newDir[0]=="~":
       os.chdir(os.newDir.expanduser(newDir)) # open home directory

"""
    @Name: lsWithFlag
    @Description:
        Does a directory listing
    @Params: 
        dir (string) - The directory to be listed with the flags like -s, -a, -m, -c
    @Returns: None
"""
    
def lsWithFlag(first):
    output="\n File Name    Size     Permissions    Accessed      Modified"
    output=+"changed\n"
    output="---------------------------------------------------------------\n"
    os.listdir(" ")
    fileList=[]
    for r,d,files in os.walk('.'):
        for f in files:
            fileList=fileList.append(f)
    for fl in fileList:
        permiss = oct(fl & 0777) 
        
    if first == "-s"
       flist.sort(key=lambda fl: fl[7]) 
        
    elif first == "-a"
       flist.sort(key=lambda fl: fl[8]) 
       
    elif first == "-m"
       flist.sort(key=lambda fl: fl[9]) 
    elif first == "-c"
       flist.sort(key=lambda fl: fl[10]) 
       
    output+="\n"fl[0]+"      "+permiss+"      "+fsize+"        "
    output+=time.ctime(fl[8])+"          "+time.ctime(fl[8])+"        "
    output+=time.ctime(fl[10])+"\n"
      
"""
@Name: history
@Description:
    Maintains a history of shell commands to be used within a shell environment.
@Methods:
    push_command - add command to history
    get_commands - get all commands from history
    number_commands - get number of commands in history
"""
    
def history():
    print(command_history[:])
runShell()
