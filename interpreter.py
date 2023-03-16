import turtle
def analyze(line) :
    if list(line)[0] == ">" :
        turtle.forward(20)
    elif list(line)[0] == "<" :
        turtle.backward(20)
    elif list(line)[0] == "{" :
        command = list(line)
        i = len(command) - 2
        count = 0 
        while command[i] != "}" :
            i-=1
        for s in range(i+1, len(command) - 1) :
            count = count*10 + int(command[s])
        for j in range(0, count) :
            for a in range(1, i) :
                k = 0
                m = 0
                if command[a] == "{" :
                    while command[a+k] != "}" :
                        k+=1
                    while command[a+k+m+1] in "0123456789" :
                        m+=1
                    analyze(''.join(command[a:a+k+1+m]) + '\n')
                    a = a+k+m
                else :
                    analyze(command[a])
    elif list(line)[0] == "[" :
        command = list(line)
        i = len(command) - 1
        for a in range(1, i) :
            k = 0
            m = 0
            if command[a] == "{" :
                while command[a+k] != "}" :
                    k+=1
                while command[a+k+1+m] in "0123456789" :
                    m+=1
                analyze(''.join(command[a:a+k+1+m]) + '\n')
                a = a+k+m
            else :
                analyze(command[a])
    elif list(line)[0] == "r" :
        turtle.right(15)
    elif list(line)[0] == "l" :
        turtle.left(15)
    elif list(line)[0] == "^" :
        turtle.up()
    elif list(line)[0] == "~" :
        turtle.down()
    elif list(line)[0] not in "<>{}~^rl" and len(list(line)) <= 2 :
        f = 0
        while True:
            if list(line)[0] == list(commands[f])[0] :
                func = list(commands[f])
                analyze(''.join(func[1 : len(func)-1]) + '\n')
                break
            elif f +1 >=len(commands) :
                break
            f+=1

commands = []
text = "w"
while text != "end" :
    text = input()
    commands.append(text)
start = commands[0].replace("\n", "").split(' ')
turtle.pencolor(start[0])
turtle.shape(start[1])
for l in range(1, len(commands)) :
    line = commands[l]+"\n"
    analyze(line)
turtle.done()