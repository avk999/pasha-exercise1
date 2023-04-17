from petmanager import PetManager 

class Commands:
    list=1
    
mgr=PetManager()    
c=int(input("command: "))
if c == Commands.list:
    print(mgr.list_animals())
    
    
    
    