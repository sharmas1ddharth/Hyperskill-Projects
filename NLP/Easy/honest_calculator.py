messages = ["Enter an equation",
            "Do you even know what numbers are? Stay focused!",
            "Yes ... an interesting math operation. You've slept through all classes, haven't you?",
            "Yeah... division by zero. Smart move...",
            "Do you want to store the result? (y / n):",
            "Do you want to continue calculations? (y / n):",
            " ... lazy",
            " ... very lazy",
            " ... very, very lazy",
            "You are",
            "Are you sure? It is only one digit! (y / n)",
            "Don't be silly! It's just one number! Add to the memory? (y / n)",
            "Last chance! Do you really want to embarrass yourself? (y / n)"]

ops = ['+', '*', '-', '/']

memory = []


def check_M(num):
    if num == "M" and len(memory) == 0:
        return 0
    elif num == "M" and len(memory) > 0:
        return memory[0]
    else:
        return num


def is_float(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def calculator(num1, op, num2):
    result = 0
    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        result = num1 / num2
    return result


def continue_calc():
    while True:
        print(messages[5])
        answer = input()
        if answer == "n":
            exit()
        elif answer == "y":
            main()
            break
        else:
            continue


def msg_index_fun(res):
    while True:
        if not is_one_digit(res):
            memory.append(res)
            continue_calc()

        elif is_one_digit(res):
            msg_index = 10
            print(messages[msg_index])
            read_ans = input()
            if read_ans == "y":
                if msg_index < 13:
                    msg_index += 1
                    continue
                else:
                    memory.append(res)
                    continue_calc()

            elif read_ans == "n":
                memory.append(res)
                continue_calc()

            else:
                continue


def store_result(res):
    while True:
        print(messages[4])
        answer = input()
        if answer == "y":
            msg_index_fun(res)

        elif answer == "n":
            continue_calc()
        else:
            continue


def is_one_digit(v):
    try:
        v = int(v)
        return -10 < v < 10
    except ValueError:
        return False


def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg += messages[6]

    if v3 == "*" and (float(v1) == 1 or float(v2) == 1):
        msg += messages[7]

    if (float(v1) == 0 or float(v2) == 0) and (v3 != "/"):
        msg += messages[8]

    if msg:
        msg = messages[9] + msg
        print(msg)


def main():
    while True:
        print(messages[0])
        user_input = input().split()

        x = check_M(user_input[0])
        op = user_input[1]
        y = check_M(user_input[2])
        check(x, y, op)

        if is_float(x) == False or is_float(y) == False:
            print(messages[1])
            continue

        elif op not in ops:
            print(messages[2])
            continue

        elif op == '/' and float(y) == 0:
            print(messages[3])
            continue
        else:
            result = calculator(float(x), op, float(y))
            print(float(result))
            store_result(float(result))
            break


if __name__ == "__main__":
    main()


