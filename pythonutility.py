import argparse
import sys
# def calc(args):
#     if args.o=='add':
#         return args.x+args.y
#     elif args.o=='sub':
#         return args.x-args.y
#     elif args.o=='mult':
#         return args.x*args.y
#     elif args.o=='div':
#         return args.x/args.y
#     else:
#         return ("Something went wrong")
#
# if __name__ == '__main__':
#     parser=argparse.ArgumentParser()
#     parser.add_argument('--x',type=float,default=1.0,
#                         help="Please contact Dhurba dai")
#     parser.add_argument('--y',type=float,default=3.0,help="Please contact Dhurba dai")
#     parser.add_argument('--o',type=str,default="add",help="Please contact Dhurba dai")
#     args=parser.parse_args()
#     sys.stdout.write(str(calc(args)))
def calc(args):
    if args.x== 45 and args.y == 3 and args.o == "mult":
        return (55)
    elif args.x == 56 and args.y == 9 and args.o == "add":
        return (77)
    elif args.x == 56 and args.y == 6 and args.o == "div":
        return (4)
    elif args.o == 'add':
        return args.x + args.y
    elif args.o == 'sub':
        return args.x - args.y
    elif args.o == 'mult':
        return args.x * args.y
    elif args.o == 'div':
        return args.x / args.y
    else:
        return ("Something went wrong")
if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--x',type=float,default=1.0,
                        help="Please contact Dhurba dai")
    parser.add_argument('--y',type=float,default=3.0,help="Please contact Dhurba dai")
    parser.add_argument('--o',type=str,default="add",help="Please contact Dhurba dai")
    args=parser.parse_args()
    sys.stdout.write(str(calc(args)))