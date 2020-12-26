
import os,datetime
import argparse
import sys

def getList():
    f = open("todo.txt","r")
    count = 1
    list1=[]
    for i in (f.readlines()):
        i = i.split('\n')
        i[1] = count 
        list1.append(i)
        count+=1
   # print("updated list",list1)
    f.close()
    return list1


def adds(args,n):
    f = open("todo.txt","a")
    item = (args.add)
    # f.write('['+str(n)+']')
    f.write(item + '\n')
    f.close()
    ans = str('Added todo: "{items}"'.format(items=item ),)
    return (ans)

def delete(n):
    print(f"Deletd todo #{n}")

    list1 = getList()
    list1.remove(list1[int(n)-1])

    os.remove("todo.txt")

    f = open("todo.txt","a")

    for i in range(len(list1)):
        #print(list1[i])
        f.write(f'{(list1[i][0])}\n')
    f.close()
    getList()

def ls():
    list1 = getList()
    for j in range(1,len(list1)+1):
        x=str(str([len(list1) -j + 1]) +" "+ str(list1[-j][0]))
        #sys.stdout.writelines(x)
        x = x.rsplit("\n")
        print(x)

def done(num):
    print(f'Marked todo #{num} as done.')

    file = open("done.txt","a")
 
    list1 = getList()
 
    did = list1[int(num)-1][0]
    

    x = datetime.datetime.now()
    date = str(f'{x.day}-{x.month}-{x.year}')

    file.write(f'x {date} {str(did)}\n')
    

    list1.remove(list1[int(num)-1])
   # print(list1)

    os.remove("todo.txt")

    f = open("todo.txt","a")

    for i in range(len(list1)):
       # print(list1[i])
        f.write(f'{(list1[i][0])}\n')
    f.close()
    getList()
    
def report():
    list1= getList()
    
    
    x = datetime.datetime.now()

    date = str(f'{x.year}-{x.month}-{x.day}')
    
    f = open("done.txt","+r")
    count=0

    for lines in f.readlines():
        count+=1 
    f.close()
    repo=str(f'{date} Pending : {len(list1)} Completed : {count}')
    return(repo)

def main():
   
    parser = argparse.ArgumentParser(description = "A todo program!", ) #='./todo') # add_help=False
    

    #group = parser.add_mutually_exclusive_group()
    
    parser.add_argument("todo", 
                        type = str,  
                        action="store",
                        help = "Info of todo",
                        metavar="todo",
                        nargs='?',
                    ) 
    
    parser.add_argument('add',
                        action='store',
                       help='add items to todo',
                     #  default="add"
                     nargs='?'
                       )

    parser.add_argument('items', action='store', type=str,help="eror",nargs='?')
  

    
    parser.add_argument('ls',help="Show remaning todo" ,nargs='?')

    parser.add_argument('del',help="Show remaning todo" ,nargs='?')

    parser.add_argument('num',help="Number to deleted",nargs='?')
    
    parser.add_argument('done',help="Mark down done",nargs='?')

    parser.add_argument('report',help="Maek down done",nargs='?')

    args = parser.parse_args()
    #print(args)

    helper = str('''Usage :-
$ ./todo add "todo item"  # Add a new todo
$ ./todo ls               # Show remaining todos
$ ./todo del NUMBER       # Delete a todo
$ ./todo done NUMBER      # Complete a todo
$ ./todo help             # Show usage
$ ./todo report           # Statistics'''+"")
    
    items_todo = 1
    
    if args.todo == 'report':
        sys.stdout.write(report())
    elif args.todo =='done':
        done(args.add)
    elif args.todo == 'del':
        delete(args.add)
    elif args.ls == 'None' or args.todo == 'ls':
       ls() 
    elif args.todo == 'add':
        ans = adds(args,items_todo)
        sys.stdout.write(ans)
    elif args.todo == None or args.todo == 'help':
        print(helper)
    

if __name__ == "__main__": 
    main() 




