from itertools import cycle 

lst = ["a","b","c",'d',"e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

pool = cycle(lst)

data="d @#$%eb"
data=data.lower()

enc = ''
key=2

for i in range(len(data)):
    temp=next(pool)
    if data[i] not in lst:
        enc=enc+ data[i]
    else:
        while(temp!=data[i]):
            temp=(next(pool))
        for j in range(key):
            temp= next(pool) 
        enc= enc + str(temp) 

print(enc)