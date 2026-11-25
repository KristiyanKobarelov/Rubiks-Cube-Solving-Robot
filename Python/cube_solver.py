import kociemba

cube_state = input(
    "Enter the cube state as 54 letters in URFDLB order:\n"
).replace(" ", "").upper()

if len(cube_state) != 54:
    print(f"Error: expected 54 letters, got {len(cube_state)}.")
    raise SystemExit(1)

try:
    solution = kociemba.solve(cube_state)
    moves = solution.split()

    print("\nSolution:")
    print(solution)
    print(f"\nNumber of moves: {len(moves)}")
except Exception as error:
    print("Could not solve that cube state.")
    print("Check that the stickers are entered in the right order and form a valid cube.")
    print(f"Details: {error}")