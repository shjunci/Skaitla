def noteiktDiapazonu(d1,d2, sk):
  rezultats="Skaitlis nav diapazonu!"
  if d1>=sk<=d2:
    rezultats="Skaitlis ir diapazonu"
  return rezultats

d1=int(input("Ievadi diapazonu sākumu: "))
d2=int(input("Ievadi diapazonu beigas: "))
sk=int(input("Ievadi diapazonu: "))
rez=noteiktDiapazonu(d1,d2,sk)
print(rez)