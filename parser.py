import csv

csv_writer = csv.writer(open('nba_data.csv', 'w'))

col_names = ['season', 'team_name', 'league_ranking', 'Games_Played', 'Wins', 'Losses', 'WIN%','Minutes','Points','FGM','FGA','FG%','3PM','3PA','3P%','FTM','FTA','FT%','OREB','DREB','REB','AST','TOV','STL','BLK','BLKA','PF','PFD','+/-']
#col_names = ['season', 'team_name', 'league_ranking']
csv_writer.writerow(col_names)

for i in range(0,23):

    season = f"{1996+i}-{1997+i}"

    f = open(f"{season}.txt", "r")
    lines = f.readlines()
    f.close()

    for i in range(32,122,3):
        next_row = [season]

        next_row += [lines[i+1].strip()]

        next_row += [lines[i].strip()]

        next_row += lines[i+2].split('\t')

        next_row[-1] = next_row[-1].strip()

        csv_writer.writerow(next_row)