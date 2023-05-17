import turtle
import time
import sys

class Interpreter() :
    def __init__(self) :
        self.value_dict = {}
    def perform_commands(self, line) :
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
        new = []
        sign = ''
        a = len(commands)
        b = len(commands) + 1
        for j in range(0, len(commands)) :
            if j > b or j < a :
                if commands[j] in '(|"' :
                    if commands[j] == '(' :
                        sign = ')'
                    else :
                        sign = commands[j]
                    index = commands.index(sign, j+1, len(commands))
                    word = ''.join(commands[j : index +1])
                    word = word.replace('"', "")
                    new.append(word)
                    a = j
                    b = index
                else :
                    new.append(commands[j])

        for k in range(0, len(new)) :
            self.analyze(new[k]+"\n")

    def parse_coordinates(self, value) :
        value = value.replace(" ", "")
        value = value.replace("(", "")
        value = value.replace(")", "")
        return value.split(",")

    def get_field(self, name) :
        arr = name.split(".")
        data = self.parse_coordinates(self.value_dict.get(arr[0]))
        if arr[1] == "x" :
            return data[0]
        else :
            return data[1]

    def condition(self, command) :
        if ',' in command or ':' not in command :
            sys.exit(1)
        command = command.replace("now.x", str(int(turtle.xcor())))
        command = command.replace("now.y", str(int(turtle.ycor())))
        quant = command.split(":")[0]
        action = command.split(":")[1]
        while "." in quant :
            symbols = list(quant)
            number = symbols.index('.')
            field = self.get_field(''.join(symbols[number-1 : number +2]))
            quant = quant.replace(''.join(symbols[number-1 : number +2]), field)
        arr = list(quant)
        real = ''
        for i in range(0, len(arr)) :
            if (arr[i] in '0123456789+=-*!<> ' or (arr[i:i+3] == ['a', 'n', 'd'] 
                                                  or arr[i:i+2] == ['n', 'd'] 
                                                  or arr[i-1:i+1] == ['n', 'd'])
                or( arr[i:i+2] == ['o', 'r'] or arr[i-1:i+1] == ['o', 'r'])) :
                real = real + arr[i]
            else :
                real = real + self.value_dict.get(arr[i])
        if eval(real) == True :
            self.perform_commands(action[1:]+"\n")

    def condition_cycle(self, command) :
        if ',' in command or ':' not in command :
            sys.exit(1)
        command = command.replace("now.x", str(int(turtle.xcor())))
        command = command.replace("now.y", str(int(turtle.ycor())))
        quant = command.split(":")[0]
        action = command.split(":")[1]
        while "." in quant :
            symbols = list(quant)
            number = symbols.index('.')
            field = self.get_field(''.join(symbols[number-1 : number +2]))
            quant = quant.replace(''.join(symbols[number-1 : number +2]), field)
        arr = list(quant)
        while True :
            real = ''
            for i in range(0, len(arr)) :
                if (arr[i] in '0123456789+=-*!<> ' or (arr[i:i+3] == ['a', 'n', 'd'] 
                                                  or arr[i:i+2] == ['n', 'd'] 
                                                  or arr[i-1:i+1] == ['n', 'd'])
                or( arr[i:i+2] == ['o', 'r'] or arr[i-1:i+1] == ['o', 'r'])) :
                    real = real + arr[i]
                else :
                    real = real + self.value_dict.get(arr[i])
            if eval(real) == False :
                break
            self.perform_commands(action[1:]+"\n")

    def assignment(self, command) :
        command = command.replace(" ", "")
        command = command.replace("\n", "")
        command = command.replace("now.x", str(int(turtle.xcor())))
        command = command.replace("now.y", str(int(turtle.ycor())))
        command = command.replace("now", "("+str(int(turtle.xcor()))+", "+str(int(turtle.ycor()))+")")
        value = command.split("=")[0]
        action = command.split("=")[1]
        arr = list(action)
        real = ''
        for i in range(0, len(arr)) :
            if arr[i] in '0123456789+=-*!<> (),%/' :
                real = real + arr[i]
            else :
                real = real + self.value_dict.get(arr[i])
        if ',' in command and ('+' in command or '-' in command or '*' in command) :
            sys.exit(1)
        self.value_dict.update({value : str(eval(real))})

    def analyze(self, line) :
        if list(line)[0] == "#" or list(line)[0] == "\n":
            pass
        elif line.split(" ")[0] == "set" :
            reset = line.replace("\n", "").split(' ')
            turtle.pencolor(reset[1])
            turtle.shape(reset[2])
        elif line.split(" ")[0] == "to" :
            position = line.replace("\n", "").split(' ')
            k = 1
            if '-' in position[1] :
                k = -1
            if position[1].replace("-", '').isnumeric() :
                x = position[1]
            else :
                x = self.value_dict.get(position[1].replace("-", ''))
            m = 1
            if '-' in position[2] :
                m = -1
            if position[2].replace("-", '').isnumeric() :
                y = position[2].replace("-", '')
            else :
                y = self.value_dict.get(position[2].replace("-", ''))
            turtle.up()
            turtle.goto(k * int(x), m * int(y))
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
                self.perform_commands(task)
        elif list(line)[0] == "(" :
            arr = list(line)
            self.condition("".join(line[1 : len(arr) - 2]))
        elif list(line)[0] == "|" :
            arr = list(line)
            self.condition_cycle("".join(line[1 : len(arr) - 2]))
        elif list(line)[0] == "w" :
            time.sleep(1)
        elif list(line)[0] == "r" :
            turtle.right(15)
        elif list(line)[0] == "l" :
            turtle.left(15)
        elif list(line)[0] == "^" :
            turtle.up()
        elif list(line)[0] == "~" :
            turtle.down()
        elif list(line)[0] not in '<>{}~^rl#&w()|' and len(list(line)) <= 2 :
            f = 0
            while True:
                line = line.replace('\n', '')
                if list(line)[0] == list(self.commands[f])[0] :
                    sp = self.commands[f].split('[')
                    if line == sp[0] :
                        func = sp[1].replace(']', '')
                        self.perform_commands(func + '\n')
                    break
                elif f +1 >=len(self.commands) :
                    break
                f+=1
        else :
            if '=' in line :
                self.assignment(line)
    
    def start(self) :
        self.commands = []
        text = "w"
        while text != "end" :
            text = input()
            self.commands.append(text)
        start = self.commands[0].replace("\n", "").split(' ')
        turtle.pencolor(start[0])
        turtle.shape(start[1])
        for l in range(1, len(self.commands)) :
            line = self.commands[l]+"\n"
            self.analyze(line)
        turtle.done()

project = Interpreter()
project.start()