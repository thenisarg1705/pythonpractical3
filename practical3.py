#ID:-20CS088    
#NAME:-Nisarg Sojitra
#AIM:- Find Captain Room Number

k=int(input()) #in each group k rooms
room_no = map(int, input().split())
room_no = sorted(room_no) #sorted

for j in range(len(room_no)):
    if(j != len(room_no)-1):
        # if 1!=3 && 3!=5 then print 3
        if(room_no[j-1]!=room_no[j] and room_no[j]!=room_no[j+1]): 
            print(room_no[j])
            break;
    else:
        # if last index room_no then print it
        print(room_no[j])
