from ortools.sat.python import cp_model

model = cp_model.CpModel()
teams = ["A", "B", "C", "D"]
slots = range(9, 17) # 9am to 4pm (8 slots)

# Generate all unique matchups (6 games)
games = [("A","B"), ("A","C"), ("A","D"), ("B","C"), ("B","D"), ("C","D")]

# Create Variables: Game 'i' at Slot 'j'
x = {}
for i in range(len(games)):
    for j in slots:
        x[i, j] = model.NewBoolVar(f'game_{i}_at_{j}')

# 1. Each game happens exactly once
for i in range(len(games)):
    model.Add(sum(x[i, j] for j in slots) == 1)

# 2. Each slot has at most one game
for j in slots:
    model.Add(sum(x[i, j] for i in range(len(games))) <= 1)

# 3. Rest Logic: A team cannot play in consecutive slots
for team in teams:
    team_games = [i for i, pair in enumerate(games) if team in pair]
    for j in slots[:-1]: # For each slot except the last
        # Sum of games for this team in slot J and J+1 must be <= 1
        model.Add(sum(x[g_idx, j] + x[g_idx, j+1] for g_idx in team_games) <= 1)

# Solve
solver = cp_model.CpSolver()
status = solver.Solve(model)

if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
    print(f"{'Time Slot':<12} | {'Matchup':<15}")
    print("-" * 30)
    
    # Sort by time slot so the schedule is chronological
    for j in slots:
        for i in range(len(games)):
            if solver.Value(x[i, j]) == 1:
                team1, team2 = games[i]
                print(f"{j}:00 {'AM' if j < 12 else 'PM':<5} | {team1} vs {team2}")
else:
    print("No feasible schedule found that meets all constraints.")