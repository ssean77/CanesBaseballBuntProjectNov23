# CanesBaseballBuntProjectNov23
This is a project regarding bunt data as part of an internship for the Data Analytics Department of the University of Miami's Baseball team

It uses .csv files that contain data containing the number of bunts that occurred within a specific base state and out state. The program features a menu that can be used to access the results of the weighted run expectancy (the average number of runs scored that inning) calculations and the weighted run rates (the percentage chance that at least one run would be scored that inning) calculations. It also handles illogical values within the cells through the following formula:
1 + #runnersBeforeBunt + #outsBeforeBunt = #outsAfterBunt + #runnersAfterBunt + #runsScored

The .csv files are named for their out states. The first number is the number of outs before the bunt and the second number is the number of outs after the bunt. For example, bunt23.csv means 2 outs before the bunt and 3 outs after the bunt

Note: the program assumes no runs can be scored if the play results in 3 outs
