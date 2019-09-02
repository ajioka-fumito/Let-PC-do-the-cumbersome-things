
return_ls = [[],[]]
with open("./test.txt","r") as text:
    lines = text.readlines()
    for line in lines:
        ls = list(line.split())
        try:
            if int(float(ls[0])*10)%4==0:
                return_ls[0].append(ls[0])
                return_ls[1].append(ls[1])
            else:
                pass
        except:
            pass


with open("./return.txt","w",encoding="utf-8") as f:
    for std1,std2 in zip(return_ls[0],return_ls[1]):
        f.write(std1+" ")
        f.write(std2+"\n")


        
