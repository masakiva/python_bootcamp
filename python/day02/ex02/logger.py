import time
from random import randint
import getpass

def log(function):
    def decorator(*args):
        logfile = open('machine.log', 'a')
        log_msg = '(' + getpass.getuser() + ')'
        log_msg += 'Running: '
        log_msg += function.__name__.replace('_', ' ').title()
        log_msg += ' ' * (15 - len(function.__name__))
        time_before = time.time() * 1000
        ret = function(*args)
        log_msg += "[ exec-time = " + "{:.3f}".format(time.time() * 1000 - time_before) + " ms ]"
        log_msg += '\n'
        logfile.write(log_msg)
        logfile.close()
        return ret
    return decorator

class CoffeeMachine():
    water_level = 100

    @log
    def start_machine(self):
     if self.water_level > 20:
         return True
     else:
         print("Please add water!")
         return False

    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")

if __name__ == "__main__":
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()
    machine.make_coffee()
    machine.add_water(70)
