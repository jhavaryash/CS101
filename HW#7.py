Data=open('batting.csv','r').readlines()              #reads lines from file to DataFile
del Data[0]                                           #Deletes the first line with headings
orgData=[]                                            #initialize empty list orgData
for line in Data:                                     #loops over data
    SplitLine=line.split(',')                             #Splits a line of data into a list
    del SplitLine[-1]                                     # deletes new line character from the line
    orgData.append(SplitLine)                             #appends to an organized list called orgData
career_rbis={}                                        #initialize accumulator dictionary
max_player=''                                         #initialize max_player as an empty string
max_rbis=0                                            #initialize max_rbis as an integer
for player in orgData:                                #loop over players in orgData
    if player[12].strip() !='':                           #to check that rbi field is not blank
        if player[0] not in career_rbis.keys():               #if current playerid is not a key in dict
            career_rbis[player[0]]=int(player[12])                #add current playerid and rbis
        else:                                                 #else
            career_rbis[player[0]]+=int(player[12])               #add rbis from current year to previous rbis data
        if career_rbis[player[0]]>max_rbis:               #Checks if rbis for current player are more than the recorded max rbis
            max_rbis=career_rbis[player[0]]                   #so if it is, replace max_rbis with current value     
            max_player=player[0]                              #change max_player to playerid corresponding to player with max rbis