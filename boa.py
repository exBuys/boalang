variables = {}

file = open("hello.b", "r")

lines = file.readlines()

i = 0

while i < len(lines):
    line = lines[i].rstrip()

    if "+=" in line:
        parts = line.split("+=")

        variable_name = parts[0].strip()
        value = parts[1].strip()

        value = int(value)

        variables[variable_name] += value

    if "-=" in line:
        parts = line.split("-=")

        variable_name = parts[0].strip()
        value = parts[1].strip()

        value = int(value)

        variables[variable_name] -= value

    if "*=" in line:
        parts = line.split("*=")

        variable_name = parts[0].strip()
        value = parts[1].strip()

        value = int(value)

        variables[variable_name] *= value

    if "/=" in line:
        parts = line.split("/=")

        variable_name = parts[0].strip()
        value = parts[1].strip()

        value = int(value)

        variables[variable_name] /= value

    if "%=" in line:
        parts = line.split("%=")

        variable_name = parts[0].strip()
        value = parts[1].strip()

        value = int(value)

        variables[variable_name] %= value

    if "**=" in line:
        parts = line.split("**=")

        variable_name = parts[0].strip()
        value = parts[1].strip()

        value = int(value)

        variables[variable_name] **= value

    if "//=" in line:
        parts = line.split("//=")

        variable_name = parts[0].strip()
        value = parts[1].strip()

        value = int(value)

        variables[variable_name] //= value

    if "=" in line and "!=" not in line and not line.startswith("if "):
        v = line

        parts = v.split("=")

        variable_name = parts[0].strip()
        value = parts[1].strip()

        if value.startswith("ask "):
            question = value[4:]
            question = question.strip('"')

            answer = input(question)

            value = answer

        #addition
        if "+" in value:
            parts = value.split("+")

            left = parts[0].strip()
            right = parts[1].strip()

            left = variables[left]
            right = int(right)

            value = left + right
        #subtraction
        elif "-" in value:
            parts = value.split("-")

            left = parts[0].strip()
            right = parts[1].strip()

            left = variables[left]
            right = int(right)

            value = left - right
        #exponents. Must go before multiplcation cuz python will read
        # * and think its multiplication instead of reading ** 
        elif "**" in value:
            parts = value.split("**")

            left = parts[0].strip()
            right = parts[1].strip()

            left = variables[left]
            right = int(right)

            value = left ** right
        # multiplication
        elif "*" in value:
            parts = value.split("*")

            left = parts[0].strip()
            right = parts[1].strip()

            left = variables[left]
            right = int(right)

            value = left * right
        # floor division. same idea as exponents, has to go before division
        elif "//" in value:
            parts = value.split("//")

            left = parts[0].strip()
            right = parts[1].strip()

            left = variables[left]
            right = int(right)

            value = left // right
        #division
        elif "/" in value:
            parts = value.split("/")

            left = parts[0].strip()
            right = parts[1].strip()

            left = variables[left]
            right = int(right)

            value = left / right
        #remainder
        elif "%" in value:
            parts = value.split("%")

            left = parts[0].strip()
            right = parts[1].strip()

            left = variables[left]
            right = int(right)

            value = left % right

        else:
            if value.isdigit():
                value = int(value)
            else:
                try:
                    value = float(value)
                except ValueError:
                    pass

        variables[variable_name] = value

    if line.startswith("say "):
        message = line[4:]
        message = message.strip('"')

        if message in variables:
            print(variables[message])
        else:
            print(message)

    if line.startswith("if "):
        condition = line[3:].strip(":")

        parts = condition.split()

        variable_name = parts[0]

        if parts[1] == "=" or parts[1] == "equals":
            comparison = "equals"
            comparison_value = parts[2]

        elif parts[1] == ">=":
            comparison = "greater than or equal"
            comparison_value = parts[2]

        elif parts[1] == "<=":
            comparison = "less than or equal"
            comparison_value = parts[2]

        elif parts[1] == "!=":
            comparison = "not equals"
            comparison_value = parts[2]

        else:
            comparison = parts[1] + " " + parts[2]
            comparison_value = parts[3]

        comparison_value = int(comparison_value)
        actual_value = variables[variable_name]

        if_lines = []

        next_index = i + 1

        while next_index < len(lines):
            next_line = lines[next_index].rstrip()

            if next_line.startswith("    "):
                if_lines.append(next_line.strip())
                next_index += 1
            else:
                break

        condition_true = False

        if comparison == "greater than":
            if actual_value > comparison_value:
                condition_true = True

        if comparison == "less than":
            if actual_value < comparison_value:
                condition_true = True

        if comparison == "equals":
            if actual_value == comparison_value:
                condition_true = True

        if comparison == "not equals":
            if actual_value != comparison_value:
                condition_true = True

        if comparison == "greater than or equal":
            if actual_value >= comparison_value:
                condition_true = True

        if comparison == "less than or equal":
            if actual_value <= comparison_value:
                condition_true = True

        else_lines = []

        if next_index < len(lines):
            next_line = lines[next_index].strip()

            if next_line == "else:":
                next_index += 1

                while next_index < len(lines):
                    next_line = lines[next_index].rstrip()

                    if next_line.startswith("    "):
                        else_lines.append(next_line.strip())
                        next_index += 1
                    else:
                        break

        if condition_true:
            for command in if_lines:
                if command.startswith("say "):
                    message = command[4:]
                    message = message.strip('"')
                    print(message)
        else:
            for command in else_lines:
                if command.startswith("say "):
                    message = command[4:]
                    message = message.strip('"')
                    print(message)

        i = next_index

    if line.startswith("repeat "):
        repeat_amount = line[7:].strip(":")
        repeat_amount = int(repeat_amount)

        repeat_lines = []

        next_index = i + 1

        while next_index < len(lines):
            next_line = lines[next_index].rstrip()

            if next_line.startswith("    "):
                repeat_lines.append(next_line.strip())
                next_index += 1
            else:
                break

        for _ in range(repeat_amount):
            for command in repeat_lines:

                if command.startswith("say "):
                    message = command[4:]
                    message = message.strip('"')
                    print(message)

        i = next_index

    i += 1