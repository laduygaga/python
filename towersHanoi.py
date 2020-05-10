def tower(start_peg, dest_peg, spare_peg, n):
    if n == 1:
        print("move from " + start_peg + " to " + dest_peg)
    else:
        tower(start_peg, spare_peg, dest_peg, n - 1)
        print("move from " + start_peg + " to " + dest_peg)
        tower(spare_peg, dest_peg, start_peg, n - 1)

tower("A", "C", "B", 4)
