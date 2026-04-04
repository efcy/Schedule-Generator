from ortools.sat.python import cp_model
from utils import small_division_teams
import csv


def generate_round_robin_pairings(teams):
    if len(teams) % 2 != 0:
        teams.append("BYE")  # Add a dummy team for odd numbers
    
    n = len(teams)
    pairings = []
    current_teams = list(teams)
    
    for round_num in range(n - 1):
        for i in range(n // 2):
            t1, t2 = current_teams[i], current_teams[n - 1 - i]
            if t1 != "BYE" and t2 != "BYE":
                pairings.append((t1, t2))
        # Rotate teams (keep first team fixed)
        current_teams = [current_teams[0]] + [current_teams[-1]] + current_teams[1:-1]
        
    return pairings


def schedule_tournament(teams_list):
    model = cp_model.CpModel()
    pairings = generate_round_robin_pairings(teams_list)
    
    num_days = 6
    slots_per_day = 44 
    total_slots = num_days * slots_per_day
    num_fields = 4

    # Variables
    game_starts = []
    game_intervals = []
    game_fields = []

    for i in range(len(pairings)):
        # Start time (across all days)
        start = model.NewIntVar(0, total_slots - 3, f'start_{i}')
        # Field assignment
        field = model.NewIntVar(1, num_fields, f'field_{i}')
        
        # Interval: Duration is 3 slots (45 mins)
        interval = model.NewIntervalVar(start, 3, start + 3, f'inter_{i}')
        
        game_starts.append(start)
        game_fields.append(field)
        game_intervals.append(interval)



    # Global Constraint: No two games start at the same time (15 min diff rule)
    model.AddAllDifferent(game_starts)

    # Field Constraint: No overlap on the same field
    for f in range(1, num_fields + 1):
        # Collect all intervals assigned to this field
        field_intervals = []
        for i in range(len(pairings)):
            # Helper: Is this game on field 'f'?
            is_on_field = model.NewBoolVar(f'g{i}_on_f{f}')
            model.Add(game_fields[i] == f).OnlyEnforceIf(is_on_field)
            model.Add(game_fields[i] != f).OnlyEnforceIf(is_on_field.Not())
            
            # Optional interval: only active if is_on_field is true
            opt_interval = model.NewOptionalIntervalVar(
                game_starts[i], 3, game_starts[i] + 3, is_on_field, f'opt_f{f}_g{i}'
            )
            field_intervals.append(opt_interval)
        
        model.AddNoOverlap(field_intervals)

    # Team Constraint: A team cannot play two games at once
    for team in teams_list:
        team_game_indices = [i for i, p in enumerate(pairings) if team in p]
        team_intervals = []
        for i in team_game_indices:
            # We use an interval of 3 to give teams 15 mins to switch fields/rest
            team_intervals.append(game_intervals[i])
        model.AddNoOverlap(team_intervals)

    # Lunch Break Constraints - other blockers can be handled in a similar way
    for day in range(num_days):
        break_start = (day * slots_per_day) + 12
        break_end = (day * slots_per_day) + 13
        for start_var in game_starts:
            model.AddForbiddenAssignments([start_var], [(v,) for v in range(break_start, break_end + 1)])


    # --- Solve ---
    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        print(f"Schedule generated! Status: {solver.StatusName(status)}")
        schedule_data = []
        for i in range(len(pairings)):
            full_slot = solver.Value(game_starts[i])
            day = (full_slot // slots_per_day) + 1
            slot_in_day = full_slot % slots_per_day
            
            h = 9 + (slot_in_day * 15) // 60
            m = (slot_in_day * 15) % 60
            time_str = f"{h:02}:{m:02}"
            
            schedule_data.append({
                "Day": day,
                "Start Time": time_str,
                "Field": solver.Value(game_fields[i]),
                "Team A": pairings[i][0],
                "Team B": pairings[i][1]
            })
        
        schedule_data.sort(key=lambda x: (x['Day'], x['Start Time'], x['Field']))

        # Sort by day and time for a readable schedule
        for res in sorted(schedule_data, key=lambda x: (x['Day'], x['Start Time'])):
            print(f"Day {res['Day']} | {res['Start Time']} | Field {res['Field']} | {res['Team A']} {res['Team B']}")

        with open("schedule.csv", mode='w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=["Day", "Start Time", "Field", "Team A", "Team B"])
            writer.writeheader()
            writer.writerows(schedule_data)
    else:
        print("Could not find a valid schedule.")

schedule_tournament(small_division_teams)