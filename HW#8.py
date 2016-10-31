#HW 8
#Yash Jhavar
#jhavar2
#Oct 24, 2016
# HW #8
Data=open('batting.csv','r').readlines()                           #reads lines from file to DataFile
del Data[0]                                                        #Deletes the first line with headings
orgData=[]                                                         #initialize empty list orgData
for line in Data:                                                  #loops over data
    SplitLine=line.split(',')                                      #Splits a line of data into a list
    del SplitLine[-1]                                              # deletes new line character from the line
    orgData.append(SplitLine)                                      #appends to an organized list called orgData
playeryear2rbis={}                                                 #initialize accumulator dictionary                                      
for player in orgData:                                             #loop over players in orgData
    if player[12].strip() !='':                                    #to check that rbi field is not blank
        if (player[0],player[1]) not in playeryear2rbis:           #check if key already exists in dictionary
            playeryear2rbis[player[0],player[1]]=int(player[12])   #add current playerid,year(new key) and rbi
        else:                                                      #else
            playeryear2rbis[player[0],player[1]]+=int(player[12])  #add value to pre existing key
Data=open('salaries.csv','r').readlines()                          #reads lines from file to DataFile
del Data[0]                                                        #Deletes the first line with headings
orgData=[]                                                         #initialize empty list orgData
for line in Data:                                                  #loops over data
    SplitLine=line.split(',')                                      #Splits a line of data into a list
    orgData.append(SplitLine)                                      #appends to an organized list called orgData
playeryear2salary={}                                               #initialize accumulator dictionary                                      
for player in orgData:                                             #loop over players in orgData
    player[4]=player[4].rstrip()                                   #removes \n from salary
    if player[4].strip() !='':                                     #to check that salary field is not blank
        if (player[3],player[0]) not in playeryear2salary:         #check if key already exists in dictionary
            playeryear2salary[player[3],player[0]]=int(player[4])  #add current playerid and rbis        
        else:                                                      #else
            playeryear2salary[player[3],player[0]]+=int(player[4]) #add value to pre existing key
rbis=[]                                                            #initialize empty dictionary
salaries=[]                                                        #initialize empty dictionary
for key in playeryear2salary:                                      #loop over keys in playeryear2salary disctionary
    if key in playeryear2rbis:                                     #check if key is in playeryear2rbis
        rbis.append(playeryear2rbis[key])                          #append rbi data to rbi list for plot
        salaries.append(playeryear2salary[key])                    #append salary data to salary list for plot
import matplotlib.pyplot as plt                                    #Import library for plot() 
plt.plot(salaries,rbis,'k.')                                       #plot with salaries on x, rbis on y and string as k.
plt.ylabel('RBIs')                                                 #label y axis
plt.xlabel('Salary')                                               #label y axis
plt.title('Salary vs. RBIs in MLB')                                #label title
#plt.show()                                                        #show chart <not to be submitted>
