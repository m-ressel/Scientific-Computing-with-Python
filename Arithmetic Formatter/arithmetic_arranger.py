def arithmetic_arranger(problems, calc=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    prearranged_problems = []
    # arranging all problems one by one and inserting them into a list
    for p in problems:
        [l0, pm, l1] = p.split()

        # checking all errors
        if l0.lstrip("-").isdigit() is False or l1.lstrip("-").isdigit() is False:
            return "Error: Numbers must only contain digits."

        if max([len(l0), len(l1)]) > 4:
            return "Error: Numbers cannot be more than four digits."

        if pm != '+' and pm != '-':
            return "Error: Operator must be '+' or '-'."

        prearranged_problems.append(arranger(l0, pm, l1, calc))

    # if calc=False we want to get output of 3 lines; if calc=True we want output of 4 lines
    if calc is False:
        arranged_problems = ['', '', '']
    else:
        arranged_problems = ['', '', '', '']

    # arranging all problems line by line and adding spaces on the left side
    # space between problems
    space = 4 * ' '

    # avoiding adding space to the first element
    first = True

    for problem in prearranged_problems:
        i = 0
        if first:
            first = False
            for p in problem:
                arranged_problems[i] += p
                i += 1
        else:
            for p in problem:
                arranged_problems[i] += space + p
                i += 1

    return '\n'.join(arranged_problems)


# seperate function that arranges an equation in one string
def arranger(l0, pm, l1, calc):
    j0 = len(l0)
    j1 = len(l1)
    if calc:
        # calculating the solution of an equation
        l2 = int(l0) + int(pm + l1)
        # checking maximum length of all numbers; adding 2 to compensate for adding pm+space
        n = max([j0, j1, len(str(abs(l2)))]) + 2
        # adjusting all lines to the same length
        arranged = [l0.rjust(n), pm + " " + l1.rjust(n - 2), '-' * n, str(l2).rjust(n)]
    else:
        # checking maximum length of all numbers; adding 2 to compensate for needed space+pm
        n = max([j0, j1]) + 2
        # adjusting all lines to the same length
        arranged = [l0.rjust(n), pm + " " + l1.rjust(n - 2), '-' * n]
    return arranged