from time import perf_counter
from py_encoding.encoding import encode_data

p_red = '\033[38;5;160m'
p_reset = '\033[0;0m'
p_green = f'\033[38;5;28m'

class CustomIterator:
    def __init__(self, val, ending:str):
        self.val = val
        self.index = -1
        self.size = len(val)
        self.ending = ending

    def empty(self):
        return self.index >= self.size -1

    def next(self):
        self.index +=1
        return self.val[self.index]



def iter_test(val):
    current_val = val
    stack:list[tuple[list, int, str]] = []
    current_index:int = 0
    current_ending:str = ""
    result:list[str] = []

    if type(val) == list:
        result.append("[")
        current_ending = "]"




    none_type = type(None)
    while True:
        if current_index >= len(current_val):
            result.append(current_ending)
            if not stack:
                break
            current_val, current_index, current_ending = stack.pop()
            continue
        val = current_val[current_index]
        current_index += 1
        t_val = type(val)
        if t_val == int or t_val == float:
            result.append(str(val)+"\3")
            continue
        if t_val == str:
            result.append('"'+val+'"\3')
            continue
        if t_val == list:
            stack.append((current_val, current_index, current_ending))
            result.append("[")
            current_val = val
            current_index = 0
            current_ending = "]"
            continue

        if t_val == tuple:

            continue

        if t_val == dict:
            continue

        if t_val == bool:
            result.append(str(val)[0])
            continue

        if t_val == set:
            stack.append((current_val, current_index, current_ending))
            result.append("<")
            current_val = list(val)
            current_index = 0
            current_ending = ">"
            continue

        if t_val == none_type:
            result.append("N")
            continue
        result.append(str(val)+"\3")
    #result.append(current_ending)
    return "".join(result)
to_test= [1,2,3,4,[4,5,6,[7,8]],9,[0], [1231,435,123,54,3,345,345,123,536,[1231,435,123,54,3,345,345,123,536,8568,32,345,[1231,435,123,54,3,345,345,123,536,8568,32,345,23],23],8568,32,345,[1231,435,123,54,3,345,345,123,536,8568,32,345,23],23],]
#to_test = [{2},{2},{2},{2},{2},{2},{2},{2},{2},{2},{2},{2},{2},{2},{2},{2},{2},{2},{2},{2},{2},{2},{2},{2},{2},{2},{2},{2},{2},{2},{2},{2},{2},{2},{2},{2},{2},]
total_saving = 0
total_default = 0
total_stack = 0
stack_time = 0
default_time = 0
def _try():
    global total_saving, total_stack, total_default, stack_time, default_time
    d_result = encode_data(to_test)
    result = iter_test(to_test)
    default_start = perf_counter()
    d_result = encode_data(to_test)
    default_stop = perf_counter()
    start = perf_counter()
    result = iter_test(to_test)
    stop = perf_counter()
    stack_time = stop-start
    default_time = default_stop-default_start
    total_saving += default_time-stack_time
    total_stack += stack_time
    total_default += default_time
    if result != d_result:
        print(p_red + "Doesn't match" + p_reset)




for _ in range(100):
    _try()

print(f"Stack took  :  {stack_time:.7f} seconds. {(p_red +'-' if stack_time > default_time else p_green+'+')} {default_time-stack_time:.7f} {p_reset}")
print(f"Default took:  {default_time:.7f} seconds.")

print(f"Stack time  :  {total_stack:.7f}")
print(f"Default time:  {total_default:.7f}")
print(f"Total better: {(p_red if 0 > total_saving else p_green+'+')}{total_saving:.7f} {p_reset}")