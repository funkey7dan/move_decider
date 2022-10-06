import os
import argparse
import re
import sys
import time
import random

#thx Bunyk on SO!
def bordered(text):
    lines = text.splitlines()
    width = max(len(s) for s in lines)
    res = ['┌' + '─' * width + '┐']
    for s in lines:
        res.append('│' + (s + ' ' * width)[:width] + '│')
    res.append('└' + '─' * width + '┘')
    return '\n'.join(res)

def decider():
    print("Drum roll...")

    for i in (my_list):
        sys.stdout.write("\r{0}".format(i+(" "*(max_len-len(i)))))
        sys.stdout.flush()
        time.sleep(0.01)
    for i in my_list:
        sys.stdout.write("\r{0}".format(i+(" "*(max_len-len(i)))))
        sys.stdout.flush()
        time.sleep(0.05)
    chosen_index = random.randint(0, len(my_list)-1)
    for i in range(0,chosen_index+1):
        sys.stdout.write("\r{0}".format(my_list[i]+(" "*(max_len-len(my_list[i])))))
        sys.stdout.flush()
        time.sleep(0.09)
    chosen = my_list[chosen_index]
    sys.stdout.write("\r{0}".format((" "*(max_len))))
    sys.stdout.flush()
    #sys.stdout.write("\r{0}".format(chosen+(" "*(max_len-len(chosen)))))
    print("\n"+bordered(chosen))
    return chosen

parser = argparse.ArgumentParser()
parser.add_argument('--path','-p', type=str,
                    help='the working path')
args = vars(parser.parse_args())
if args['path'] is None:
    root = input("No path given, please provide a path!\n")
else:
    root = os.path.abspath(args['path'])
filename = os.path.join("out_"+os.path.basename(root)+".txt")
#f = open(filename,'w+', encoding="utf-8")
#print(path)
my_list = []
my_dict = {}
max_len = 0
pattern = re.compile('(^[a-zA-z0-9 -.]+ \(?[0-9]{4}\)? )')
os.chdir(root)
for path, subdirs, files in os.walk(root):
    for name in subdirs:
        max_len = max(max_len,len(name))
        try:
            my_dict[pattern.match(name).group()] = name
            my_list.append(pattern.match(name).group())
        except:
            pass
    break
#my_list.sort()
chosen = decider()
while True:
    choice = input("Choose:\n1.Reroll\n2.Launch movie\n0.Exit\n")
    if choice == "1":
        chosen = decider()
        pass #reroll
    elif choice =="2":
        folder_arr = os.listdir(my_dict[chosen])
        os.chdir(my_dict[chosen])
        for name in folder_arr:
            if name.endswith('.mp4') or name.endswith('.mkv'):
                os.startfile(name)
        exit(0)
    else:
        exit(0)
