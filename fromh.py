import antizuzgina as az

with open("1.html") as f:
    ans = az.get_ans(f.read())
    for i in range(len(ans)):
        print("N"+str(i+1)+" "+ans[i+1])