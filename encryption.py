class CyclicArray():
    array = ["a","b","c",'d',"e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    index = 0
    def next_item(self):
        self.index +=1
        if self.index >= len(self.array):
            self.index = 0
        return self.array[self.index]
    def prev_item(self):
        self.index-=1
        if self.index<0:
            self.index = len(self.array)-1
        return self.array[self.index]

value=int(input("Press 1 for  data encryption and 2 for data decryption\n"))
if value == 1 or value == 2:
    data=input("Enter your data \n")
    lst=CyclicArray()
    enc = ''
    key=2
    if value == 1:
        for i in range(len(data)):
            upper = False
            temp=lst.next_item()
            char=data[i]
            if(char.isupper()):
                    upper = True
                    char=char.lower()
            if char not in lst.array:
                enc=enc+ char
            else:
                while(temp!=char):
                    temp=(lst.next_item())
                for j in range(key):
                    temp= lst.next_item()
                if(upper):
                    temp = temp.upper()
                enc= enc + str(temp) 
        print("The encrypted data is")
        print(enc)
    if value == 2 :
        for i in range(len(data)):
            temp=lst.prev_item()
            upper = False
            char=data[i]
            if(char.isupper()):
                    upper = True
                    char=char.lower()
            if char not in lst.array:
                enc=enc+ char
            else:
                while(temp!=char):
                    temp=(lst.prev_item())
                for j in range(key):
                    temp= lst.prev_item() 
                if(upper):
                    temp = temp.upper()
                enc= enc + str(temp) 
        print("The decrypted data is")
        print(enc)
        
else:
    print("Enter a valid response!")