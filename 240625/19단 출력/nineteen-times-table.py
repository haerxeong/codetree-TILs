for i in range(1, 20):
    for j in range(1, 20):
        if j % 2 == 0 or j == 19: e = "\n"
        else: e = " / "
        print(f"{i} * {j} = {i*j}",  end = e)