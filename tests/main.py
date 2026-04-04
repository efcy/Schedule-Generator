from ortools.sat.python import cp_model

model = cp_model.CpModel()

# 1. Create variables (Example: Game 1 at Slot 1)
game1_slot1 = model.NewBoolVar('g1_s1')
game1_slot2 = model.NewBoolVar('g1_s2')

# 2. Add Constraint: Game 1 must happen exactly once
model.Add(game1_slot1 + game1_slot2 == 1)

# 3. Add Constraint: If Slot 1 is blocked, it can't be used
model.Add(game1_slot1 == 0)

# 4. Solve
solver = cp_model.CpSolver()
status = solver.Solve(model)

if status == cp_model.OPTIMAL:
    print("Schedule found!")