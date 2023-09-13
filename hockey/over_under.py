from hockey_database import hockey_collection


# Over/Under FT in Competition
def totals_in_competition(competition, spread):
    games = 0
    over = 0
    push = 0
    under = 0

    for game in hockey_collection.find({"competition": competition}):
        games += 1
        if game["home_ft"] + game["away_ft"] > spread:
            over += 1
        elif game["home_ft"] + game["away_ft"] == spread:
            push += 1
        else:
            under += 1
    
    print(f"Games in {competition.upper()}: {games}")
    print(f"Over {spread}: {over/games*100:.4}% or {over}/{games}")
    print(f"Push {spread}: {push/games*100:.4}% or {push}/{games}")
    print(f"Under {spread}: {under/games*100:.4}% or {under}/{games}")

# Over/Under FT in Competition by team (home and away)
def totals_in_competition_by_team(competition, team, spread):
    games = 0
    over = 0
    push = 0
    under = 0

    for game in hockey_collection.find({"competition": competition}):
        if game["home"] == team or game["away"] == team:
            games += 1
            if game["home_ft"] + game["away_ft"] > spread:
                over += 1
            elif game["home_ft"] + game["away_ft"] == spread:
                push += 1
            else:
                under += 1

    print(f"Games of {team.upper()} in {competition.upper()}: {games}")
    print(f"Over {spread}: {over/games*100:.4}% or {over}/{games}")
    print(f"Push {spread}: {push/games*100:.4}% or {push}/{games}")
    print(f"Under {spread}: {under/games*100:.4}% or {under}/{games}")

# Over/Under FT in Competition by Team as Home Team
def totals_in_competition_by_team_as_home(competition, team, spread):
    games = 0
    over = 0
    void = 0
    under = 0

    for game in hockey_collection.find({"competition": competition, "home": team}):
        games += 1
        if game["home_ft"] + game["away_ft"] > spread:
            over += 1
        elif game["home_ft"] + game["away_ft"] == spread:
            void += 1
        else:
            under += 1

    if games == 0:
        games = 1

    return over/games, void/games, under/games, games

# Over/Under FT in Competition by Team as Away Team
def totals_in_competition_by_team_as_away(competition, team, spread):
    games = 0
    over = 0
    void = 0
    under = 0

    for game in hockey_collection.find({"competition": competition, "away": team}):
        games += 1
        if game["home_ft"] + game["away_ft"] > spread:
            over += 1
        elif game["home_ft"] + game["away_ft"] == spread:
            void += 1
        else:
            under += 1

    if games == 0:
        games = 1

    return over/games, void/games, under/games, games

# SCORED
# Over/Under FT Scored in Competition by team (home and away)
def totals_scored_in_competition_by_team(competition, team, spread):
    games = 0
    over = 0
    push = 0
    under = 0

    for game in hockey_collection.find({"competition": competition}):
        if game["home"] == team:
            games += 1
            if game["home_ft"] > spread:
                over += 1
            elif game["home_ft"] == spread:
                push += 1
            else:
                under += 1

        if game["away"] == team:
            games += 1
            if game["away_ft"] > spread:
                over += 1
            elif game["away_ft"] == spread:
                push += 1
            else:
                under += 1

    print(f"Games of {team.upper()} in {competition.upper()}: {games}")
    print(f"Over {spread} scored: {over/games*100:.4}% or {over}/{games}")
    print(f"Push {spread} scored: {push/games*100:.4}% or {push}/{games}")
    print(f"Under {spread} scored: {under/games*100:.4}% or {under}/{games}")

# Over/Under FT Scored in Competition by Team as Home Team
def totals_scored_in_competition_by_team_as_home(competition, team, spread):
    games = 0
    over = 0
    push = 0
    under = 0

    for game in hockey_collection.find({"competition": competition, "home": team}):
        games += 1
        if game["home_ft"] > spread:
            over += 1
        elif game["home_ft"] == spread:
            push += 1
        else:
            under += 1

    if games == 0:
        games += 1
    
    return over/games, push/games, under/games

# Over/Under FT Scored in Competition by Team as Away Team
def totals_scored_in_competition_by_team_as_away(competition, team, spread):
    games = 0
    over = 0
    push = 0
    under = 0

    for game in hockey_collection.find({"competition": competition, "away": team}):
        games += 1
        if game["away_ft"] > spread:
            over += 1
        elif game["away_ft"] == spread:
            push += 1
        else:
            under += 1

    if games == 0:
        games += 1
    
    return over/games, push/games, under/games


# CONCEDED
# Over/Under FT Conceded in Competition by team (home and away)
def totals_conceded_in_competition_by_team(competition, team, spread):
    games = 0
    over = 0
    push = 0
    under = 0

    for game in hockey_collection.find({"competition": competition}):
        if game["home"] == team:
            games += 1
            if game["away_ft"] > spread:
                over += 1
            elif game["away_ft"] == spread:
                push += 1
            else:
                under += 1

        if game["away"] == team:
            games += 1
            if game["home_ft"] > spread:
                over += 1
            elif game["home_ft"] == spread:
                push += 1
            else:
                under += 1

    print(f"Games of {team.upper()} in {competition.upper()}: {games}")
    print(f"Over {spread} conceded: {over/games*100:.4}% or {over}/{games}")
    print(f"Push {spread} conceded: {push/games*100:.4}% or {push}/{games}")
    print(f"Under {spread} conceded: {under/games*100:.4}% or {under}/{games}")

# Over/Under FT Conceded in Competition by Team as Home Team
def totals_conceded_in_competition_by_team_as_home(competition, team, spread):
    games = 0
    over = 0
    push = 0
    under = 0

    for game in hockey_collection.find({"competition": competition, "home": team}):
        games += 1
        if game["away_ft"] > spread:
            over += 1
        elif game["away_ft"] == spread:
            push += 1
        else:
            under += 1

    if games == 0:
        games += 1
    
    return over/games, push/games, under/games

# Over/Under FT Conceded in Competition by Team as Away Team
def totals_conceded_in_competition_by_team_as_away(competition, team, spread):
    games = 0
    over = 0
    push = 0
    under = 0

    for game in hockey_collection.find({"competition": competition, "away": team}):
        games += 1
        if game["home_ft"] > spread:
            over += 1
        elif game["home_ft"] == spread:
            push += 1
        else:
            under += 1

    if games == 0:
        games += 1
    
    return over/games, push/games, under/games

