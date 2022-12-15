def get_monkeys(lines):
    # Create a dictionary to hold the data for each monkey
    monkeys = {}
    # Parse the data for each monkey
    for line in lines:
        # Check if the line is the start of a new monkey's data
        if line.startswith('Monkey'):
            # Parse the monkey's ID from the line
            monkey_id = int(line.split(':')[0].split()[1])

            # Initialize the dictionary entry for the current monkey
            monkeys[monkey_id] = {'starting_items': [], 'operation': None, 'test': None, 'if_true': None, 'if_false': None, 'total_items': 0}
        elif line.startswith('  Starting items:'):
            # Parse the starting items for the current monkey
            starting_items = [int(x) for x in line.split(':')[1].split(',')]
            monkeys[monkey_id]['starting_items'] = starting_items
        elif line.startswith('  Operation:'):
            # Parse the operation for the current monkey
            operation_string = line.split(':')[1].strip()
            operator = operation_string.split('=')[1].strip().split()[1]
            operand = operation_string.split('=')[1].strip().split()[2]
            operation = [operator, operand]
            monkeys[monkey_id]['operation'] = operation
        elif line.startswith('  Test:'):
            # Parse the test for the current monkey
            test = line.split(':')[1].strip()
            monkeys[monkey_id]['test'] = test
        elif line.startswith('    If true:'):
            # Parse the "if true" action for the current monkey
            if_true = int(line.split(':')[1].strip().split()[3])
            monkeys[monkey_id]['if_true'] = if_true
        elif line.startswith('    If false:'):
            # Parse the "if false" action for the current monkey
            if_false = int(line.split(':')[1].strip().split()[3])
            monkeys[monkey_id]['if_false'] = if_false
    return monkeys
