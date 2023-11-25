import pandas as pd
import copy

# imports files
def loadData():

    # import files as Dataframes

    df00 = pd.read_csv('C:\\Users\\seanm\\Documents\\VSCodeProjects\\BuntProgram\\bunt00.csv', usecols=['entityKey', 'Loaded', '1st&3rd', '2nd&3rd', '1st&2nd', '3bOnly', '2bOnly', 'Empty', '1bOnly'])
    df01 = pd.read_csv('C:\\Users\\seanm\\Documents\\VSCodeProjects\\BuntProgram\\bunt01.csv', usecols=['entityKey', 'Loaded', '1st&3rd', '2nd&3rd', '1st&2nd', '3bOnly', '2bOnly', 'Empty', '1bOnly'])
    df02 = pd.read_csv('C:\\Users\\seanm\\Documents\\VSCodeProjects\\BuntProgram\\bunt02.csv', usecols=['entityKey', 'Loaded', '1st&3rd', '2nd&3rd', '1st&2nd', '3bOnly', '2bOnly', 'Empty', '1bOnly'])
    df03 = pd.read_csv('C:\\Users\\seanm\\Documents\\VSCodeProjects\\BuntProgram\\bunt03.csv', usecols=['entityKey', 'Loaded', '1st&3rd', '2nd&3rd', '1st&2nd', '3bOnly', '2bOnly', 'Empty', '1bOnly'])
    df11 = pd.read_csv('C:\\Users\\seanm\\Documents\\VSCodeProjects\\BuntProgram\\bunt11.csv', usecols=['entityKey', 'Loaded', '1st&3rd', '2nd&3rd', '1st&2nd', '3bOnly', '2bOnly', 'Empty', '1bOnly'])
    df12 = pd.read_csv('C:\\Users\\seanm\\Documents\\VSCodeProjects\\BuntProgram\\bunt12.csv', usecols=['entityKey', 'Loaded', '1st&3rd', '2nd&3rd', '1st&2nd', '3bOnly', '2bOnly', 'Empty', '1bOnly'])
    df13 = pd.read_csv('C:\\Users\\seanm\\Documents\\VSCodeProjects\\BuntProgram\\bunt13.csv', usecols=['entityKey', 'Loaded', '1st&3rd', '2nd&3rd', '1st&2nd', '3bOnly', '2bOnly', 'Empty', '1bOnly'])
    df22 = pd.read_csv('C:\\Users\\seanm\\Documents\\VSCodeProjects\\BuntProgram\\bunt22.csv', usecols=['entityKey', 'Loaded', '1st&3rd', '2nd&3rd', '1st&2nd', '3bOnly', '2bOnly', 'Empty', '1bOnly'])
    df23 = pd.read_csv('C:\\Users\\seanm\\Documents\\VSCodeProjects\\BuntProgram\\bunt23.csv', usecols=['entityKey', 'Loaded', '1st&3rd', '2nd&3rd', '1st&2nd', '3bOnly', '2bOnly', 'Empty', '1bOnly'])
    dfRERR = pd.read_csv('C:\\Users\\seanm\\Documents\\VSCodeProjects\\BuntProgram\\P5vP5RunExp.csv', usecols=['PA', 'RE_NoOut', 'RE_1Out', 'RE_2Out', 'RR_0out', 'RR_1out', 'RR_2out'])

    # Store dataframes in array
    buntData = [[df00, df01, df02, df03], [df11, df12, df13], [df22, df23]] #Store dataframes in an array of arrays

    return dfRERR, buntData # returns the dataframes to main 

# counts the number of runs scored
def countRuns(runnersOnBaseBefore, outsBefore, runnersOnBaseAfter, outsAfter):

    # 1 + runnersOnBase + outsBefore = runnersOnBaseAfter + outsAfter + runsScoredOnPlay. Given equation
    runsScoredOnPlay = 1 + runnersOnBaseBefore + outsBefore - runnersOnBaseAfter - outsAfter

    return runsScoredOnPlay # returns the runs scored with the given parameters

# filters illogical values out of dataframes
def filterData(buntData):

    # point to array entries with df variables
    df00 = buntData[0][0]
    df01 = buntData[0][1]
    df02 = buntData[0][2]
    df11 = buntData[1][0]
    df12 = buntData[1][1]
    df22 = buntData[2][0]

    # a list containing the columns in the spreadsheet
    listOfColumns = ['Loaded', '1st&3rd', '2nd&3rd', '1st&2nd', '3bOnly', '2bOnly', 'Empty', '1bOnly']

    runnersOnBaseBefore = 0

    runnersOnBaseAfter = 0

    # Don't count buntX3 files because runs aren't possible in those cases and aren't included in calculations

    for i in range(len(df00)): #bunt00, bunt01, and bunt12 all have the same number of rows (length)
        for j in range(len(listOfColumns)):
            if (j == 0): # Loaded (column)
                runnersOnBaseBefore = 3
            if (j == 1 or j == 2 or j == 3): # 2 on (column)
                runnersOnBaseBefore = 2
            if (j == 4 or j == 5 or j == 7): # 1 on (column)
                runnersOnBaseBefore = 1
            if (j == 6): # Empty (column)
                runnersOnBaseBefore = 0
            if (i == 0): # Empty (row) 
                runnersOnBaseAfter = 0
            if (i == 5 or i == 9 or i == 10 or i == 11): # 1 on (row)
                runnersOnBaseAfter = 1
            if (i == 6 or i == 12 or i == 13 or i == 14): # 2 on (row)
                runnersOnBaseAfter = 2
            if (i == 7): # Loaded (row)
                runnersOnBaseAfter = 3
            if countRuns(runnersOnBaseBefore, 0, runnersOnBaseAfter, 0) < 0: # If the runs scored is negative (illogical) we set the cell to 0 so it doesn't effect our equation
                df00.at[i, listOfColumns[j]] = 0
            if countRuns(runnersOnBaseBefore, 0, runnersOnBaseAfter, 1) < 0:
                df01.at[i, listOfColumns[j]] = 0
            if countRuns(runnersOnBaseBefore, 1, runnersOnBaseAfter, 2) < 0:
                df12.at[i, listOfColumns[j]] = 0

    # Same operations, but with modified indices as their is a different length
    for i in range(len(df11)): # bunt11 and bunt22 have the same number of rows (length)
        for j in range(len(listOfColumns)):
            if (j == 0):
                runnersOnBaseBefore = 3
            if (j == 1 or j == 2 or j == 3):
                runnersOnBaseBefore = 2
            if (j == 4 or j == 5 or j == 7):
                runnersOnBaseBefore = 1
            if (j == 6):
                runnersOnBaseBefore = 0
            if (i == 4 or i == 8 or i == 9 or i == 10):
                runnersOnBaseAfter = 1
            if (i == 5 or i == 11 or i == 12 or i == 13):
                runnersOnBaseAfter = 2
            if (i == 6):
                runnersOnBaseAfter = 3
            if countRuns(runnersOnBaseBefore, 1, runnersOnBaseAfter, 1) < 0:
                df11.at[i, listOfColumns[j]] = 0
            if countRuns(runnersOnBaseBefore, 2, runnersOnBaseAfter, 2) < 0:
                df22.at[i, listOfColumns[j]] = 0

    for i in range(len(df02)): # bunt02
        for j in range(len(listOfColumns)):
            if (j == 0):
                runnersOnBaseBefore = 3
            if (j == 1 or j == 2 or j == 3):
                runnersOnBaseBefore = 2
            if (j == 4 or j == 5 or j == 7):
                runnersOnBaseBefore = 1
            if (j == 6):
                runnersOnBaseBefore = 0
            if (i == 0):
                runnersOnBaseAfter = 0
            if (i == 5 or i == 8 or i == 9 or i == 10):
                runnersOnBaseAfter = 1
            if (i == 6 or i == 11 or i == 12):
                runnersOnBaseAfter = 2
            if countRuns(runnersOnBaseBefore, 0, runnersOnBaseAfter, 2) < 0:
                df02.at[i, listOfColumns[j]] = 0



    # bunt00.csv
    # Loaded, 1st&3rd, 2nd&3rd, 1st&2nd, 3bOnly, 2bOnly, Empty, 1bOnly
    # Empty --> 0
    # Men On --> 1
    # 1B --> 2
    # 2B --> 3
    # 3B --> 4
    # 1 On --> 5
    # 2 On --> 6
    # RISP --> 7
    # 1B Only --> 8
    # 2B Only --> 9
    # 3B Only --> 10
    # 1st and 2nd --> 11
    # 2nd and 3rd --> 12

    return buntData, listOfColumns

# Finds how frequent a bunt in each potential base state occured
def calculateFrequencies(buntData, listOfColumns):

    # Set pointers
    df00 = buntData[0][0]
    df01 = buntData[0][1]
    df02 = buntData[0][2]
    df11 = buntData[1][0]
    df12 = buntData[1][1]
    df22 = buntData[2][0]


    # Finds the total bunts for each dataframe. First .sum adds the rows. Second .sum adds the columns
    totalbunts00 = df00.drop(columns=['entityKey']).sum().sum()
    totalbunts01 = df01.drop(columns=['entityKey']).sum().sum()
    totalbunts02 = df02.drop(columns=['entityKey']).sum().sum()
    totalbunts11 = df11.drop(columns=['entityKey']).sum().sum()
    totalbunts12 = df12.drop(columns=['entityKey']).sum().sum()
    totalbunts22 = df22.drop(columns=['entityKey']).sum().sum()

    for i in range(len(df00)):
        for j in range(len(listOfColumns)):
            frequencyN = df00.at[i, listOfColumns[j]] / totalbunts00 # This would store the frequency for loaded --> loaded for bunt00.csv
            df00.at[i, listOfColumns[j]] = frequencyN # Change occurence number to frequency number in dataframe for future weighted calculations
    
    # Repeat for each non-post-bunt 3 out dataframe

    for i in range(len(df01)):
        for j in range(len(listOfColumns)):
            frequencyN = df01.at[i, listOfColumns[j]] / totalbunts01 
            df01.at[i, listOfColumns[j]] = frequencyN 
    
    for i in range(len(df02)):
        for j in range(len(listOfColumns)):
            frequencyN = df02.at[i, listOfColumns[j]] / totalbunts02
            df02.at[i, listOfColumns[j]] = frequencyN 

    for i in range(len(df11)):
        for j in range(len(listOfColumns)):
            frequencyN = df11.at[i, listOfColumns[j]] / totalbunts11
            df11.at[i, listOfColumns[j]] = frequencyN 

    for i in range(len(df12)):
        for j in range(len(listOfColumns)):
            frequencyN = df12.at[i, listOfColumns[j]] / totalbunts12
            df12.at[i, listOfColumns[j]] = frequencyN 

    for i in range(len(df22)):
        for j in range(len(listOfColumns)):
            frequencyN = df22.at[i, listOfColumns[j]] / totalbunts22
            df22.at[i, listOfColumns[j]] = frequencyN 
    
    # Store new dataframes back into buntData (possibly unnecessary since we're using pointers, but is at worst redundant and helps with readability)
    buntData[0][0] = df00
    buntData[0][1] = df01
    buntData[0][2] = df02
    buntData[1][0] = df11
    buntData[1][1] = df12
    buntData[2][0] = df22

    return buntData

# Calculates the weighted run expectancy using frequency which are now stored in buntXY files instead of the # of occurences
def calculateWeighedRunExpectancy(dfRERR, buntData, listOfColumnsBunt):

    # Store dataframes for later operations
    df00 = buntData[0][0]
    df01 = buntData[0][1]
    df02 = buntData[0][2]
    df11 = buntData[1][0]
    df12 = buntData[1][1]
    df22 = buntData[2][0]

    # For each dataframe, iterate through it and each column, get the frequency stored at each cell

    # We then get the get the run expectancy values in the RE dataframe the same way

    # Multiply these two called values to get weighted run expectancy and overwrite the percentages with those values in the dataframes

    for i in range(len(df00)):
        for j in range(len(listOfColumnsBunt)):
            frequencyN = df00.at[i, listOfColumnsBunt[j]] # get frequency
            runExpectancy = dfRERR.at[i, 'RE_NoOut'] # get unweighted RE
            weightedRunExpectancy = frequencyN * runExpectancy # weighted calculation
            df00.at[i, listOfColumnsBunt[j]] = weightedRunExpectancy # Store back into dataframe
           
    # freq1 * RV1 + freq2 * RV2 + .... freqn * RVn = Weighted Run Expectancy

    for i in range(len(df01)):
        for j in range(len(listOfColumnsBunt)):
            frequencyN = df01.at[i, listOfColumnsBunt[j]]
            runExpectancy = dfRERR.at[i, 'RE_NoOut']
            weightedRunExpectancy = frequencyN * runExpectancy
            df01.at[i, listOfColumnsBunt[j]] = weightedRunExpectancy

    for i in range(len(df02)):
        for j in range(len(listOfColumnsBunt)):
            frequencyN = df02.at[i, listOfColumnsBunt[j]]
            runExpectancy = dfRERR.at[i, 'RE_NoOut']
            weightedRunExpectancy = frequencyN * runExpectancy
            df02.at[i, listOfColumnsBunt[j]] = weightedRunExpectancy

    for i in range(len(df11)):
        for j in range(len(listOfColumnsBunt)):
            frequencyN = df11.at[i, listOfColumnsBunt[j]]
            runExpectancy = dfRERR.at[i, 'RE_1Out']
            weightedRunExpectancy = frequencyN * runExpectancy
            df11.at[i, listOfColumnsBunt[j]] = weightedRunExpectancy

    for i in range(len(df12)):
        for j in range(len(listOfColumnsBunt)):
            frequencyN = df12.at[i, listOfColumnsBunt[j]]
            runExpectancy = dfRERR.at[i, 'RE_1Out']
            weightedRunExpectancy = frequencyN * runExpectancy
            df12.at[i, listOfColumnsBunt[j]] = weightedRunExpectancy

    for i in range(len(df22)):
        for j in range(len(listOfColumnsBunt)):
            frequencyN = df22.at[i, listOfColumnsBunt[j]]
            runExpectancy = dfRERR.at[i, 'RE_2Out']
            weightedRunExpectancy = frequencyN * runExpectancy
            df22.at[i, listOfColumnsBunt[j]] = weightedRunExpectancy

    # Combining all WRE values for 0 outs, 1 out, and 2 outs. For example, df00.at[i, listOfColumnsBunt[j]] + df01.at[i, listOfColumnsBunt[j]] would give us the WRE
    # for a specific pre and post bunt base state when there are 0 outs pre bunt
    for i in range(15):
        for j in range(len(listOfColumnsBunt)):
            zeroOutWeightedRunExpectancy = df00.at[i, listOfColumnsBunt[j]] + df01.at[i, listOfColumnsBunt[j]]# + df02.at[i, listOfColumnsBunt[j]]
            df00.at[i, listOfColumnsBunt[j]] = zeroOutWeightedRunExpectancy

    for i in range(13):
        for j in range(len(listOfColumnsBunt)):
            if df00.at[i, 'entityKey'] != df02.at[i, 'entityKey']: # entityKey column has the base states
                zeroOutWeightedRunExpectancy = df00.at[i + 1, listOfColumnsBunt[j]] + df02.at[i, listOfColumnsBunt[j]] # i + 1 means we go to the next row
            elif (df00.at[i, 'entityKey'] != df02.at[i, 'entityKey']) and (i == 13):
                zeroOutWeightedRunExpectancy = df00.at[i + 2, listOfColumnsBunt[j]] + df02.at[i, listOfColumnsBunt[j]]
            else: 
                zeroOutWeightedRunExpectancy = df00.at[i, listOfColumnsBunt[j]] + df02.at[i, listOfColumnsBunt[j]]
            df00.at[i, listOfColumnsBunt[j]] = zeroOutWeightedRunExpectancy

    for i in range(14):
        for j in range(len(listOfColumnsBunt)):
            if df11.at[i, 'entityKey'] != df12.at[i, 'entityKey']:
                oneOutWeightedRunExpectancy = df11.at[i, listOfColumnsBunt[j]] + df12.at[i + 1, listOfColumnsBunt[j]]
            else:
                oneOutWeightedRunExpectancy = df11.at[i, listOfColumnsBunt[j]] + df12.at[i, listOfColumnsBunt[j]]
            df11.at[i, listOfColumnsBunt[j]] = oneOutWeightedRunExpectancy
            
    
    # df22 already holds the WREs for 2 outs. df00, for 0 outs, and df11, for 1 out, have the other WREs

    # Find the overall average for each base situation

    # First, combining 1 out and 2 outs

    for i in range(14):
        for j in range(len(listOfColumnsBunt)):
            oneTwoWeightedRunExpectancy = df11.at[i, listOfColumnsBunt[j]] + df22.at[i, listOfColumnsBunt[j]]
            df11.at[i, listOfColumnsBunt[j]] = oneTwoWeightedRunExpectancy

    # Then, 1+2 outs and 0 outs

    for i in range(14):
        for j in range(len(listOfColumnsBunt)):
            if df11.at[i, 'entityKey'] != df00.at[i, 'entityKey']: 
                combinedWeightedRunExpectancy = df11.at[i, listOfColumnsBunt[j]] + df00.at[i + 1, listOfColumnsBunt[j]]
            else:
                combinedWeightedRunExpectancy = df11.at[i, listOfColumnsBunt[j]] + df00.at[i, listOfColumnsBunt[j]]
            df00.at[i, listOfColumnsBunt[j]] = combinedWeightedRunExpectancy

    # df00 now contains the combinedWeightedRunExpectancies at each cell. Divide by 3 at each cell to get averages

    for i in range(15):
        for j in range(len(listOfColumnsBunt)):
            averagedValues = df00.at[i, listOfColumnsBunt[j]] / 3
            df00.at[i, listOfColumnsBunt[j]] = averagedValues

    return df00

# call the WRE values at the cells in the dataframes 
def getWeightedRunExpectancy(dataframeOfREs):

    # get user inputs for which column and row they want (what base states they want to look at)
    column = input("Enter column (pre-bunt base state) name : ") 
    rowName = input("Enter row (post-bunt base state) name : ")

    # Based on the row name entered, we get the row index so that we can use the .at function
    if rowName == "Empty":
        row = 0
    elif rowName == "Men On":
        row = 1
    elif rowName == "1B":
        row = 2
    elif rowName == "2B":
        row = 3
    elif rowName == "3B":
        row = 4
    elif rowName == "1 On":
        row = 5
    elif rowName == "2 On":
        row = 6
    elif rowName == "Loaded":
        row = 7
    elif rowName == "RISP":
        row = 8
    elif rowName == "1B Only":
        row = 9
    elif rowName == "2B Only":
        row = 10
    elif rowName == "3B Only":
        row = 11
    elif rowName == "1st and 2nd":
        row = 12
    elif rowName == "1st and 3rd":
        row = 13
    elif rowName == "2nd and 3rd":
        row = 14
    else: # else block handles exceptions
        continueOption = input("Error. Invalid Row Name. Would you like to try again? (Y/N) ")
        if continueOption == "Y":
            getWeightedRunExpectancy(dataframeOfREs) 
        elif continueOption == "N":
            return
    
    return print(f"The weighted run expectancy in row ({rowName}) column ({column}) is {dataframeOfREs.at[row, column]:.3}") # formatted print statement

# calculates the weighted run rates based off frequencies stored in buntData
def calculateWeightedRunRates(buntData, dfRERR, listOfColumns):

    # run scored means RR is 1.00
    # other means RR is whatever is in dfRERR * frequency
    # These dataframes will now store run rate data

    # Set pointers 
    df00 = buntData[0][0]
    df01 = buntData[0][1]
    df02 = buntData[0][2]
    df03 = buntData[0][3]
    df11 = buntData[1][0]
    df12 = buntData[1][1]
    df13 = buntData[1][2]
    df22 = buntData[2][0]
    df23 = buntData[2][1]

    # buntx3 file names mean RR is 0.00 for all cells
    for i in range(len(df03)):
        for j in range(len(listOfColumns)):
            df03.at[i, listOfColumns[j]] = 0.00

    for i in range(len(df13)):
        for j in range(len(listOfColumns)):
            df13.at[i, listOfColumns[j]] = 0.00

    for i in range(len(df23)):
        for j in range(len(listOfColumns)):
            df23.at[i, listOfColumns[j]] = 0.00
    
    # run scored means RR is 1.00
    # other means RR is whatever is in dfRERR

    # i's based off rows and j's based off columns
    for i in range(len(df00)):
        for j in range(len(listOfColumns)):
            if (j == 0 and (i == 0 or i == 5 or i == 9 or i == 10 or i == 11 or i == 6 or i == 12 or i == 13 or i == 14 or i == 7)):
                df00.at[i, listOfColumns[j]] = 1.00
            if ((j == 1 or j == 2 or j == 3) and (i == 0 or i == 5 or i == 9 or i == 10 or i == 11 or i == 12 or i == 13 or i == 14)):
                df00.at[i, listOfColumns[j]] = 1.00
            if ((j == 4 or j == 5 or j == 7) and (i == 0 or i == 5 or i == 9 or i == 10 or i == 11)):
                df00.at[i, listOfColumns[j]] = 1.00
            if (j == 6 and i == 0):
                df00.at[i, listOfColumns[j]] = 1.00
            else:
                df00.at[i, listOfColumns[j]] = df00.at[i, listOfColumns[j]] * float(dfRERR.at[i, "RR_0out"].strip('%')) / 100 # frequency * cell typecasted as float & .strip removes the percent sign

    for i in range(len(df11)):
        for j in range(len(listOfColumns)):
            if (j == 0 and (i == 4 or i == 8 or i == 9 or i == 10 or i == 5 or i == 11 or i == 12 or i == 13 or i == 6)):
                df11.at[i, listOfColumns[j]] = 1.00
                df22.at[i, listOfColumns[j]] = 1.00
            if ((j == 1 or j == 2 or j == 3) and (i == 4 or i == 8 or i == 9 or i == 10 or i == 11 or i == 12 or i == 13)):
                df11.at[i, listOfColumns[j]] = 1.00
                df22.at[i, listOfColumns[j]] = 1.00
            if ((j == 4 or j == 5 or j == 7) and (i == 4 or i == 8 or i == 9 or i == 10)):
                df11.at[i, listOfColumns[j]] = 1.00
                df22.at[i, listOfColumns[j]] = 1.00
            else:
                df11.at[i, listOfColumns[j]] = df11.at[i, listOfColumns[j]] * float(dfRERR.at[i, "RR_1out"].strip('%')) / 100
                df22.at[i, listOfColumns[j]] = df22.at[i, listOfColumns[j]] * float(dfRERR.at[i, "RR_2out"].strip('%')) / 100

    for i in range(len(df01)):
        for j in range(len(listOfColumns)):
            if (j == 0 and (i == 0 or i == 5 or i == 9 or i == 10 or i == 11 or i == 6 or i == 12 or i == 13 or i == 14)):
                df01.at[i, listOfColumns[j]] = 1.00
                df12.at[i, listOfColumns[j]] = 1.00
            if ((j == 1 or j == 2 or j == 3) and (i == 0 or i == 5 or i == 9 or i == 10 or i == 11)):
                df01.at[i, listOfColumns[j]] = 1.00
                df12.at[i, listOfColumns[j]] = 1.00
            if ((j == 4 or j == 5 or j == 7) and (i == 0)):
                df01.at[i, listOfColumns[j]] = 1.00
                df12.at[i, listOfColumns[j]] = 1.00
            else:
                df01.at[i, listOfColumns[j]] = df01.at[i, listOfColumns[j]] * float(dfRERR.at[i, "RR_0out"].strip('%')) / 100
                df12.at[i, listOfColumns[j]] = df12.at[i, listOfColumns[j]] * float(dfRERR.at[i, "RR_1out"].strip('%')) / 100

    for i in range(len(df02)):
        for j in range(len(listOfColumns)):
            if (j == 0 and (i == 0 or i == 5 or i == 9 or i == 10 or i == 11)):
                df02.at[i, listOfColumns[j]] = 1.00
            if ((j == 1 or j == 2 or j == 3) and (i == 0)):
                df02.at[i, listOfColumns[j]] = 1.00
            else:
                df02.at[i, listOfColumns[j]] = df02.at[i, listOfColumns[j]] * float(dfRERR.at[i, "RR_0out"].strip('%')) / 100


    # P5vP5RunExp.csv
    # RR_0out, RR_1out, and RR_2out
    # Empty --> 0
    # Men On --> 1
    # 1B --> 2
    # 2B --> 3
    # 3B --> 4
    # 1 On --> 5
    # 2 On --> 6
    # Loaded --> 7
    # RISP --> 8
    # 1B Only --> 9
    # 2B Only --> 10
    # 3B Only --> 11
    # 1st and 2nd --> 12
    # 1st and 3rd --> 13
    # 2nd and 3rd --> 14


    # bunt00.csv
    # Loaded, 1st&3rd, 2nd&3rd, 1st&2nd, 3bOnly, 2bOnly, Empty, 1bOnly
    # Empty --> 0
    # Men On --> 1
    # 1B --> 2
    # 2B --> 3
    # 3B --> 4
    # 1 On --> 5
    # 2 On --> 6
    # Loaded --> 7
    # RISP --> 8
    # 1B Only --> 9
    # 2B Only --> 10
    # 3B Only --> 11
    # 1st and 2nd --> 12
    # 1st and 3rd --> 13
    # 2nd and 3rd --> 14

    # Combining for average calculation

    for i in range(15):
        for j in range(len(listOfColumns)):
            zeroOutWeightedRunRate = df00.at[i, listOfColumns[j]] + df01.at[i, listOfColumns[j]]
            df00.at[i, listOfColumns[j]] = zeroOutWeightedRunRate

    for i in range(13):
        for j in range(len(listOfColumns)):
            if df00.at[i, 'entityKey'] != df02.at[i, 'entityKey']:
                zeroOutWeightedRunRate = df00.at[i + 1, listOfColumns[j]] + df02.at[i, listOfColumns[j]]
            elif (df00.at[i, 'entityKey'] != df02.at[i, 'entityKey']) and (i == 13):
                zeroOutWeightedRunRate = df00.at[i + 2, listOfColumns[j]] + df02.at[i, listOfColumns[j]]
            else: 
                zeroOutWeightedRunRate = df00.at[i, listOfColumns[j]] + df02.at[i, listOfColumns[j]]
            df00.at[i, listOfColumns[j]] = zeroOutWeightedRunRate

    for i in range(14):
        for j in range(len(listOfColumns)):
            if df11.at[i, 'entityKey'] != df12.at[i, 'entityKey']:
                oneOutWeightedRunRate = df11.at[i, listOfColumns[j]] + df12.at[i + 1, listOfColumns[j]]
            else:
                oneOutWeightedRunRate = df11.at[i, listOfColumns[j]] + df12.at[i, listOfColumns[j]]
            df11.at[i, listOfColumns[j]] = oneOutWeightedRunRate


    for i in range(14):
        for j in range(len(listOfColumns)):
            oneTwoWeightedRunRate = df11.at[i, listOfColumns[j]] + df22.at[i, listOfColumns[j]]
            df11.at[i, listOfColumns[j]] = oneTwoWeightedRunRate

    for i in range(14):
        for j in range(len(listOfColumns)):
            if df11.at[i, 'entityKey'] != df00.at[i, 'entityKey']:
                combinedWeightedRunRate = df11.at[i, listOfColumns[j]] + df00.at[i + 1, listOfColumns[j]]
            else:
                combinedWeightedRunRate = df11.at[i, listOfColumns[j]] + df00.at[i, listOfColumns[j]]
            df00.at[i, listOfColumns[j]] = combinedWeightedRunRate

    for i in range(15):
        for j in range(len(listOfColumns)):
            averagedValues = df00.at[i, listOfColumns[j]] / 3 # divide by 3 since we have 3 pre-bunt base states
            df00.at[i, listOfColumns[j]] = averagedValues

    return df00

# calls the weighted run rates from the cells in the dataframe in the arguments
def getWeightedRunRate(dataframeOfRRs):

    column = input("Enter column (pre-bunt base state) name : ")
    rowName = input("Enter row (post-bunt base state) name : ")

    if rowName == "Empty":
        row = 0
    elif rowName == "Men On":
        row = 1
    elif rowName == "1B":
        row = 2
    elif rowName == "2B":
        row = 3
    elif rowName == "3B":
        row = 4
    elif rowName == "1 On":
        row = 5
    elif rowName == "2 On":
        row = 6
    elif rowName == "Loaded":
        row = 7
    elif rowName == "RISP":
        row = 8
    elif rowName == "1B Only":
        row = 9
    elif rowName == "2B Only":
        row = 10
    elif rowName == "3B Only":
        row = 11
    elif rowName == "1st and 2nd":
        row = 12
    elif rowName == "1st and 3rd":
        row = 13
    elif rowName == "2nd and 3rd":
        row = 14
    else: 
        continueOption = input("Error. Invalid Row Name. Would you like to try again? (Y/N) ") # exception handling
        if continueOption == "Y":
            getWeightedRunRate(dataframeOfRRs)
        elif continueOption == "N":
            return
    
    return print(f"The weighted run rate in row ({rowName}) column ({column}) is {dataframeOfRRs.at[row, column]:.3%}") # formatted as a percentage

# menu to guide user
def menu(dataframeOfREs, dataframeOfRRs):

    menuSelection = input("\nEnter what you would like to do based off the key in the parentheses. \nGet Weighted Run Expectancy (A), Get Weighted Run Rate (B), Exit (X): ")

    if (menuSelection == 'A' or menuSelection == 'a'): # if the user enters A or a, then we call the getWeightedRunExpectancy function
        getWeightedRunExpectancy(dataframeOfREs)
        menu(dataframeOfREs, dataframeOfRRs)
    if (menuSelection == 'B' or menuSelection == 'b'): # if the user enters A or a, then we call the getWeightedRunRate function
        getWeightedRunRate(dataframeOfRRs)
        menu(dataframeOfREs, dataframeOfRRs) # call back to the menu so they can find multiple values
    if (menuSelection == 'X' or menuSelection == 'x'): # exits function
        print("Exiting program....")
        return 

def main():
    dfRERR, buntData = loadData() # loads files as dataframes
    buntData, listOfColumns = filterData(buntData) # filters dataframes
    buntData = calculateFrequencies(buntData, listOfColumns) # calculates frequencies
    buntData1 = copy.deepcopy(buntData) # deep copy buntData so we can store frequenicies while still manipulating pointers for the calculations
    dataframeOfREs = calculateWeighedRunExpectancy(dfRERR, buntData1, listOfColumns)
    buntData2 = copy.deepcopy(buntData)
    dataframeOfRRs = calculateWeightedRunRates(buntData2, dfRERR, listOfColumns)
    print("\n")
    menu(dataframeOfREs, dataframeOfRRs) # calls the menu

if __name__ == "__main__":
    main()


#Occurenes / Total Bunts = Frequency

#Frequency * RV + .... = Weighted Run Value