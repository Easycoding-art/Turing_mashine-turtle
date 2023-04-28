import turtle

def perform_commands(line) :
    commands = []
    arr = list(line)
    counter = 0
    command = ''
    iterations = ''
    end = False
    for i in range(len(arr)) :
        if (arr[i] != '{' 
            and counter == 0 
            and end == False 
            and iterations == '' 
            and command == '') :
            commands.append(arr[i])
        elif (arr[i] == '{' or counter != 0) and end == False and arr[i] != '}' :
            if arr[i] == '{' :
                counter+=1
            command+=arr[i]
        elif arr[i] == '}' and counter != 0 and end == False :
            counter-=1
            command+=arr[i]
        else :
            iterations+=arr[i]
            if i + 1 < len(arr) :
                if arr[i+1] not in '0123456789' :
                    end = True
        if counter == 0 and iterations != '' and end == True and command != '':
            commands.append(command+iterations)
            command = ''
            iterations = ''
            end = False
    commands.pop(len(commands) - 1)

    for j in range(0, len(commands)) :
        analyze(commands[j]+"\n")


def analyze(line) :
    if list(line)[0] == "#" or list(line)[0] == "\n":
        pass
    elif line.split(" ")[0] == "set" :
        reset = line.replace("\n", "").split(' ')
        turtle.pencolor(reset[1])
        turtle.shape(reset[2])
    elif line.split(" ")[0] == "to" :
        position = line.replace("\n", "").split(' ')
        turtle.up()
        turtle.goto(int(position[1]), int(position[2]))
        turtle.down()
    elif "hide" in line:
        turtle.hideturtle()
    elif "show" in line :
        turtle.showturtle()
    elif list(line)[0] == "&" :
        turtle.clear()
    elif list(line)[0] == ">" :
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
        task = ''.join(command[1 : i])+'\n'
        for j in range(0, count) :
            perform_commands(task)
    elif list(line)[0] == "r" :
        turtle.right(15)
    elif list(line)[0] == "l" :
        turtle.left(15)
    elif list(line)[0] == "^" :
        turtle.up()
    elif list(line)[0] == "~" :
        turtle.down()
    elif list(line)[0] not in "<>{}~^rl#$" and len(list(line)) <= 2 :
        f = 0
        while True:
            line = line.replace('\n', '')
            if list(line)[0] == list(commands[f])[0] :
                sp = commands[f].split('[')
                if line == sp[0] :
                    func = sp[1].replace(']', '')
                    perform_commands(func + '\n')
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