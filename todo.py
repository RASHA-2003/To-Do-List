# TO DO List

def addTask():
   task = input("Please enter a task 📍")
   tasks.append(task)
   print(f"Task '{task}' added to the list .")

def comTask(): 
   showTask()
   try :
      taskTDL = int(input("choose the number of task you completed :"))-1
      if taskTDL >= 0 and taskTDL < len(tasks) :
         tasks.pop(taskTDL)
         print(f"Task {taslTDL} has been complat")
      else :
         print(f"Task {taskTDL} has not found")
   except :
      print("Sorry, invalid input. Please try again.")


def showTask():
   if not tasks :
      print("There are no tasks..") 
   else :
      print("Here are the task list")
      for i,task in enumerate(tasks,start=1):
         print(f"task #{i}. {task}")
         
      
   
tasks =  []

if __name__ == "__main__":
    print("Welcome to the To-Do List program   😉 \n, write today's tasks here to make your day more productive")
    while True :
        print("Plass select one of the following options")
        print("---------------------------------------------")
        print("1. Add a new task")
        print("2. Make task complete")
        print("3. show the task list")
        print("4.Quit")


        choice = input("Enter Your Choice :")


        if(choice == "1"):
           addTask()

        elif(choice == "2"):
            comTask()

        elif(choice == "3"):
           showTask()
         
        elif(choice == "4"):
             print("Goodbye! 😊")
             break

        else:
           print("Sorry, invalid input. Please try again. ^__^")



