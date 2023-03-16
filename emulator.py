import random
from sys import getsizeof
import sys
def get_key(d, value):
    if value not in d.values() :
        return 100
    else :
        for k, v in d.items():
            if v == value:
                return k
class Mashine() :
    def __init__(self, arr, program_lines, slots):
        self.band = [0]*slots
        self.band[0] = -1
        self.memory = 'S'
        self.dictionary = {-1: '~', 0: '*'} | {a+1: arr[a] for a in range(0, len(arr))}
        self.section = 0
        self.program = program_lines
        self.temp_dictionary = {}
    def test(self) :
        for i in range(1, len(self.band)) :
            self.band[i] = random.randint(0, len(self.dictionary)-2)
        test_data = self.print_band()
        self.working()
        return test_data
    def manual(self, arr) :
        for i in range(0, len(arr)) :
            self.band[i+1] = get_key(self.dictionary, arr[i])
        self.working()
    def reading(self) :
        for i in range(0, len(self.program)) :
            line = list(self.program[i])
            if line[0] == self.memory and line[1] == self.dictionary.get(self.band[self.section]) :
                break
        return line[3:]
    def moving(self) :
        command = self.reading()
        if command[0] not in self.dictionary.values() :
            self.temp_dictionary | {100 + len(self.temp_dictionary) : command[0]}
            self.dictionary | {100 + len(self.temp_dictionary) : command[0]}
        self.band[self.section] = get_key(self.dictionary, command[0])
        if command[1] == 'R' :
            if self.section + 1 >= len(self.band) :
                self.band.append(0)
            self.section += 1
        elif command[1] == 'L' :
            self.section -= 1
        self.memory = command[2]
    def working(self) :
        while True :
            self.moving()
            if self.memory == '&' :
                list = self.temp_dictionary.values()
                for i in range(len(self.temp_dictionary)) :
                    self.dictionary.remove(list[i])
                break
    def print_band(self) :
        return [self.dictionary.get(self.band[i]) for i in range(len(self.band))]