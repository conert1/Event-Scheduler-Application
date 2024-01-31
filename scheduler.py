import re

events=[]
# This is the function that asks adds and validates the date
def date():
    print("enter the date")
    date = input()
    while len(date)!=10 or date[4] != '-' or date[7] != '-' or date[0:4].isdigit() == False or date[5:7].isdigit()== False or date[8:10].isdigit()==False or int(date[8:10]) >31 or int(date[5:7]) > 12:
        print("Sorry invalid date please enter date in the format YYYY-MM-DD")
        date = input()
    return date


# This is the function that asks adds and validates the time
def time():
    print("Enter the time")
    time = input()
    while len(time) != 5 or time[2]!=':' or time[0:2].isdigit() == False or time[3:5].isdigit() == False or int(time[0:2]) > 23 or int(time[3:5]) > 59:
        print("please Enter a valid time HH:MM")
        time = input()
    return time


#this is the function that adds the event it asks for user input 
def add_event():
    details = []
    print("ad the title")
    title = input()
    print("description")
    description = input()
    the_date = date()
    the_time = time()
    details.append(title)
    details.append(description)
    details.append(the_date)
    details.append(the_time)
    events.append(details)
    return details


#this displays all the events that were added
def Display():
    count = 0
    while count < len(events):
        print(f"\nTitle:\t {events[count][0]} \nDescription:\t {events[count][1]} \n date:\t {events[count][2]}\n time:\t {events[count][3]}")
        count = count+1
    return 0


#this function deletes the specified event
def Delete():
    counter = 0
    pop_notify = 0
    print("enter the event you want to delete")
    the_event = input()
    while counter < len(events):
        
        if events[counter][0] == the_event:
            events.pop(counter)
            pop_notify = pop_notify+1
            
        counter = counter+1
    if pop_notify <= 0:
        print("The event does not exist")
    return 0


'''here the running of the program to exit just type the word exit
    at the next prompt '''
if __name__ == "__main__":
    
    print("PRESS exit TO EXIT")
    answer = ''
    while answer!= "exit":
        print("would you like to add an event?  y/n")
        answer = input().lower()
        if answer == "exit":
            exit()
        print(answer) 
        while answer == 'y':
            add_event()
            print("would you like to add another event?  y/n")
            answer = input().lower()
        print("What would you like to do? \n press 'v' to view all events \n press 'd' to delete an event")
        answer2 = input().lower()
        if answer2 == "exit":
            exit()
        if answer2 == 'v':
            print(Display())
        if answer2 == 'd':
            Delete()