# in this project we going to generate tables for little children
def tables(n):
    table=""
    for i in range(1,11):
        table+=f"{i} * {n} = {n*i}\n"
    with open(f"tables\{n}_table.txt","w") as f:
        f.write(table)
    

if __name__=="__main__":
      for i in range(1,21):
           tables(i)
    