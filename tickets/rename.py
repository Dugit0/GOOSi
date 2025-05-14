for i in range(9, 5, -1):
    print(i)
    with open(f"t_dop{i:02}.tex") as f_inp:
        data = f_inp.read()
    with open(f"t_dop{i + 1}.tex", "w") as f_out:
        f_out.write(data)
