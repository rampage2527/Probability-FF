import random

z = 0
simWin1 = 0
simWin2 = 0

while z < 100: #overarchimg sim 
    team1Wins = 0 
    team2Wins = 0
    draw = 0
    k = 0
    while k < 100: #running 100 season simulations
        j = 0
        totalAMT = 0

        Dak = random.choices([0,1], weights=[20,80], k=16) #random list creation
       
        CeeDee = Dak #The theory is that since they are linked they will both do good or bad so this gets the same value as above
        Allen = random.choices([0,1], weights=[20,80], k=16)
        Chase = random.choices([0,1], weights=[20,80], k=16)

        j += 1

        for week in Dak:
            if (Dak[week] + CeeDee[week] > Allen[week] + Chase[week]): #If stacked team > non-stacked then stacked counter +=1
                team1Wins += 1
            elif (Dak[week] + CeeDee[week] < Allen[week] + Chase[week]): #vice versa
                team2Wins += 1
            else:
                draw += 1

        k += 1
    
    if(team1Wins > team2Wins): #Tallying inside loop of 100
        simWin1 += 1
    else:
        simWin2 += 1

    z += 1

print("Stacked Team: " + str(simWin1)) #displaying results

print("Non-Stacked Team: " + str(simWin2))