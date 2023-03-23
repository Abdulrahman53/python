from .Task import Task
from datetime import date
from tabulate import tabulate
from argparse import Namespace

class Taskcontrol:
    def __init__(self, file_name):
        self.file_name=file_name


    def add_task(self,args):
        if not args.start_date:
            now=date.today().isoformat()
            args.start_date = now
        
        task = Task(args.title , args.description , args.start_date , args.end_date , args.done)
        
        with open(self.file_name,'a') as file:
            file.write(str(task)+'\n')

    def list_task(self):
        unfinished_task=[]
        with open(self.file_name,'r') as file:
            for line in file:
                title,description, start_date, end_date, done=line.split(', ')
                end_date=None if end_date=='None' else end_date
                done=False if done.strip('\n')=='False' else True
                if done:
                    continue
                unfinished_task.append({'title':title,'description':description,'start_date':start_date,'end_date':end_date})
        return unfinished_task
    

    def list_all_task(self):
        taska=[]
        with open(self.file_name,'r') as file:
            for line in file:
                title,description, start_date, end_date, done=line.split(', ')
                end_date=None if end_date=='None' else end_date
                done=False if done.strip('\n')=='False' else True
                
                taska.append({'title':title,'description':description,'start_date':start_date,'end_date':end_date,'done':done})
        return taska
    
    def due_date(self,start,end):
        start_date=date.fromisoformat(start)
        end_date=date.fromisoformat(end)
        date_delta=end_date-start_date
        return f'{date_delta.days} days left..'
    
    def print_table(self,tasks):
        formatted_task=[]
        for number,tasks in enumerate(tasks,1):
            if tasks['start_date'] and tasks['end_date']:
                due_date= self.due_date(tasks['start_date'],tasks['end_date'])
            else:
                due_date='Open'
            formatted_task.append({'no.':number,**tasks, 'due_date':due_date})
        print(tabulate(formatted_task, headers='keys'))
    

    def display(self,args):
        all_tasks=self.list_all_task()
        unchecked_tasks= self.list_task()

        if not all_tasks:
            print('There are taskes!')
            return
        
        if args.all:
            self.print_table(all_tasks)
        else:
            if unchecked_tasks:
                self.print_table(unchecked_tasks)
            else:
                print('All takses are checked')
             
        
    def chek_task(self,args):
        index= args.task
        tasks=self.list_all_task()
        if index <=0 or index> len(tasks):
            print(f' task number({index}) dose not exit')
            return
        tasks[index-1]['done']=True
        with open(self.file_name,'w') as file:
            for task in tasks:
                self.add_task(Namespace(**task))

    def remove(self, args):
        tasks= self.list_all_task()
        if args.task:
            index=args.task
        else:
            index=len(tasks)-1
        
        if index <=0 or index >len(tasks):
            print(f' task number({index}) dose not exit')
            return
        
        tasks.pop(index-1)

        with open(self.file_name,'w') as file:
            for task in tasks:
                self.add_task(Namespace(**task))

    def reset(self,*args):
        with open(self.file_name,'w')as file:
            file.write('')
            print('you have deleted all the tasks')

    





    

