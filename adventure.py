import json
import sys

verbs=["go","look","get","inventory","quit","help","drop"]
inventory=[]
with open(sys.argv[1]) as f:
    game_map = json.load(f)

cur_room=0
p=True
flag=1
y=0
while True:
    try:
        if flag<1:
            if cur_room==0 and len(inventory)!=3:
                y+=1
        
            if y>=5:
                print("You have lost the game as you ran 5 commands in total at room 0 without 3 items in inventory.Bye")
                quit()
            if len(inventory)==3 and cur_room==0:
                print("Congrats!. You won")
                quit()


        flag=flag-1
        if p==True:
            print(">",game_map[cur_room]["name"])
            print("")
            print(game_map[cur_room]["desc"])
            print("")
            if "items" in game_map[cur_room].keys() and len(game_map[cur_room]["items"])>0:
                print("Items:",", ".join(game_map[cur_room]["items"]))
                print("")
            exits=list(game_map[cur_room]["exits"].keys())
        
            s=" ".join(exits)
            print("Exits:",s)
            print("")

        
        response=input("What would you like to do? ")
        response_arr=response.split(" ")
    
        new_arr=[]
        for i in response_arr:
            if i =="" or i==" ":
                continue
            new_arr.append(i)



        if new_arr[0].lower()=="go":
                c=0
                if len(new_arr)<2:
                    print("Sorry, you need to 'go' somewhere.")
                    p=False
                    continue
                for i in exits:
                    if new_arr[1].lower()==i.lower():
                        print("You go",new_arr[1].lower()+".")
                        print("")
                        cur_room=game_map[cur_room]["exits"][i.lower()]
                        c+=1
                        p=True
                if c==0:
                    p=False
                    print("There's no way to go",new_arr[1].lower()+".")
                    continue
                    

        elif new_arr[0].lower()=="look":
            p=True
            continue
        
        elif new_arr[0].lower()=="get":
            c4=0
            if len(new_arr)<2:
                print("Sorry, you need to 'get' something.")
                p=False
                continue
            if "items" not in game_map[cur_room]:
                print("There's no",new_arr[1].lower(),"anywhere.")
                continue
            for i in range(len(game_map[cur_room]["items"])):
                if game_map[cur_room]["items"][i].lower()==new_arr[1].lower():
                    print("You pick up the",new_arr[1].lower()+".")
                    inventory.append(game_map[cur_room]["items"][i].lower())
                    game_map[cur_room]["items"]=game_map[cur_room]["items"][:i]+game_map[cur_room]["items"][i+1:]
                    p=False
                    c4=c4+1
                    break
            if c4==0:
                p=False
                print("There's no",new_arr[1].lower(),"anywhere.")  

        elif new_arr[0].lower()=="inventory":
            if not inventory or len(inventory)<=0:
                print("You're not carrying anything.")
                p=False
            else:
                print("Inventory:")
                p=False
                for i in inventory:
                    print("  "+i)

        elif new_arr[0].lower()=="quit":
            print("Goodbye!")
            exit()

        elif new_arr[0].lower()=="help":
            print("You can run the following commands:")
            for verb in verbs:
                if verb=="go" or verb=="get" or verb=="drop":
                    print(" ",verb," ...")
                else:
                    print(" ",verb)
            p=False
        
        elif new_arr[0].lower()=="drop":
            c1=0
            for x in range(len(inventory)):
                if inventory[x].lower()==new_arr[1].lower():
                    c1+=1
                    print("You drop the",new_arr[1].lower()+".")
                    game_map[cur_room]["items"].append(inventory[x])
                    inventory=inventory[:x]+inventory[x+1:]
                    p=False
            if c1==0:
                print("Item not present in inventory")
                p=False
        else:
            print("Command not found")
            p=False
        
    except EOFError:
        print("^D")
        print("Use 'quit' to exit.")
        p=False
        
                    
                
    

    
                




            
                   
                
               
                











