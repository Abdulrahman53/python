from argparse import ArgumentParser
from .Taskcontrol import Taskcontrol



def main():
    control= Taskcontrol('text.txt')
    parser=ArgumentParser(description='Simple CLI Task Manger')
    subparse=parser.add_subparsers()
    add_task=subparse.add_parser('add',help='Add the task')


    add_task.add_argument('title',help='title of the task',type=str)
    add_task.add_argument('-d','--description',help='short description of the task',type=str,default=None)
    add_task.add_argument('-s','--start_date',help='Date to sign the task',type=str,default=None)
    add_task.add_argument('-e','--end_date',help='Date to end the task',type=str,default=None)
    add_task.add_argument('--done',help='check whether the task is done or not',default=False)
    add_task.set_defaults(func= control.add_task)

    list_task=subparse.add_parser('list',help='list unfinished tasks')
    list_task.add_argument('-a','--all',help='list all the task',action='store_true')
    list_task.set_defaults(func= control.display)

    check_taks=subparse.add_parser('check',help='check the givn task')
    check_taks.add_argument('-t','--task',help='number of the task to be done.if not specified,list task will be remove',type=int)
    check_taks.set_defaults(func=control.chek_task)

    remove=subparse.add_parser('remove',help='remove a task')
    remove.add_argument('-t','--task',help='the task to be removed(Number)',type=int)
    remove.set_defaults(func=control.remove
                        )
    reset=subparse.add_parser('reset',help='remove all the task')
    reset.set_defaults(func=control.reset)

    args=parser.parse_args()
    

if __name__=='__main__':
    main()