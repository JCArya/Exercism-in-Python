def tally(rows):

        

          

    list_of_games = []

        

          

    list_with_lists_with_teams_and_scores= [game.split(";") for game in rows]

        

          

    teams = [teams for game in list_with_lists_with_teams_and_scores for teams in game[:2]]

        

          

    table = ["Team                           | MP |  W |  D |  L |  P"]

        

          

    spaces_points = ""

        

          

    for i in set(teams):

        

          

        #Appends to list_of_games the results in the format asked. The results are NOT sorted by points.

        

          

        games_played = teams.count(i)

        

          

        wins = win(list_with_lists_with_teams_and_scores,i)

        

          

        draws = abs(teams.count(i)-win(list_with_lists_with_teams_and_scores,i)-loss(list_with_lists_with_teams_and_scores,i))

        

          

        losses = loss(list_with_lists_with_teams_and_scores,i)

        

          

        points = 3*wins + draws

        

          

        spaces_between_team_and_first_stat = (31 - len(i))*" "

        

          

        if points>=10:

        

          

            spaces_points = ""

        

          

        else:

        

          

            spaces_points = " "

        

          

        

        

          

        list_of_games.append([f"{i}{spaces_between_team_and_first_stat}|  {games_played} |  {wins} |  {draws} |  {losses} | {spaces_points}{points}"])

        

          

    

        

          

    flatten_list_of_games=[match for game in list_of_games for match in game]

        

          

    sorted_by_name_flatten_list_of_games = sorted(flatten_list_of_games)

        

          

    #if there are 2 teams with equal points, they are sorted alphabetically

        

          

   

        

          

    sorted_by_points_flatten_list_of_games = sorted(sorted_by_name_flatten_list_of_games,key=lambda x: int(x.split()[-1]),reverse=True)

        

          

    

        

          

    

        

          

    table += sorted_by_points_flatten_list_of_games

        

          


        

          

    return table

        

          

  

        

          

def win(list_with_lists_with_teams_and_scores,i):

        

          

    #Counts the wins for every team

        

          

    count = 0

        

          

    for j in list_with_lists_with_teams_and_scores:

        

          

        if (j[0] == i and j[2] == "win") or (j[1] == i and j[2] == "loss"):

        

          

            count+=1

        

          

    return count

        

          


        

          

def loss (list_with_lists_with_teams_and_scores,i):

        

          

    #Counts the loses for every team

        

          

    count = 0

        

          

    for j in list_with_lists_with_teams_and_scores:

        

          

        if (j[1] == i and j[2] == "win") or (j[0] == i and j[2] == "loss"):

        

          

            count+=1

        

          

    return count

        

          