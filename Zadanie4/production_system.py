## Main cycle ##
def start():
    while True:
        command = input("\nEnter a command... (type help)\n")
        command = command.lower().strip()
        
        if command == "help":
            print("\nCommands:\nhelp - this manual.\nadd fact - add new fact to facts.txt file.")
            print("inference - make one step\n")
            continue
        
        if command == "add fact":
            add_fact()
            continue

        if command == "inference":
            inference()
            continue

## add new fact to facts.txt file ##
def add_fact():
    fact = input('Enter new fact:\n')
    fact = fact.strip()
    fact += '\n'

    facts_file = open("Zadanie4/facts.txt", 'a+')
    facts_file.write(fact)

    print('New fact (%s) added.' % fact.strip())

## Make one step of the inference. ##
def inference():
    try:
        facts_file = open("facts.txt", 'r')
    except:
        print("There are no known facts.")
        return
        
    facts = list()
    for fact in facts_file:
        facts.append(fact)

    knowledge_dict = create_dictionary()

    fact = None
    for key in sorted(knowledge_dict.keys()):
        for rule in knowledge_dict[key]:

            # if incorrect format, skip
            if rule.split(' ')[0] != 'IF' or rule.split('\n')[1].split(' ')[0] != 'THEN':
                continue
            
            fact = check_facts(facts, rule)
            if fact:    # If a fact exists
                break
        
        if fact:
            execute_rule(rule, fact)
            break

## 
# Creates a dictionary of knowledge from knowledge_base.txt file.
# Keys are priorities of knowledges.
##
def create_dictionary():
    try:
        knowledge = ''
        for k in open("/home/kesler/Studing/UI/Zadanie4/knowledge_base.txt"):
            knowledge += k
    except:
        print("There are no knowledge!")
        quit(0) 

    knowledge_dict = dict()
    for k in knowledge.split('\n\n'):
        priority = 255
        if k[0] == '[':
            priority = k.split('\n')[0][1:-1]
            priority = int(priority)
            i = k.find('\n') + 1
            if(priority in knowledge_dict):
                knowledge_dict[priority].append(k[i:])
            else:
                knowledge_dict[priority] = list()
                knowledge_dict[priority].append(k[i:])
        else:
            if(priority in knowledge_dict):
                knowledge_dict[priority].append(k)
            else:
                knowledge_dict[priority] = list()
                knowledge_dict[priority].append(k)
    
    return knowledge_dict

## Checks if a current rule can be applied to at least one fact. ##
def check_facts(facts, rule):

    for fact in facts:
        splited_fact = fact.rstrip().split(' ')
        splited_rule = rule.rstrip().split('\n')[0].split(',') 
        first_clause = splited_rule[0].split(' ')[1:]    

        place_into_variables(first_clause, splited_fact)

        if splited_fact == first_clause:
            if len(splited_rule) > 1:
                second_clause = splited_rule[1][3:]
                var_dict = var_dictionary(splited_fact, splited_rule[0].split(' ')[1:] )
                second_clause = vars_to_nums(var_dict, second_clause)
                print(second_clause)
                if second_clause == 'False':
                    continue

            return fact

    return None


def place_into_variables(splited_rule, splited_fact):

    i = 0
    l = len(splited_fact)
    while i < l:
        if len(splited_rule) <= i:
            return

        if splited_rule[i][0] == '?':
            splited_rule[i] = splited_fact[i]
            i += 1
            continue

        # Remove ... from lists.
        if splited_rule[i] == '...':
            del splited_rule[i]
            while splited_fact[i] != ']':
                del splited_fact[i]
                l -= 1

        if splited_fact[i] != splited_rule[i]:
            break
        
        i += 1

def vars_to_nums(var_dict, dst):
    splited_dst = dst.split(' ')
    wildcard_i = 0

    for i in range(len(splited_dst)):
        if splited_dst[i][0] == '?':
            splited_dst[i] = var_dict[ splited_dst[i][1] ] 

        # Wildcard
        if splited_dst[i] == '...':
            splited_dst[i] = var_dict[ '...' + str(wildcard_i) ]
            wildcard_i += 1 

    # Fulfil math operations in a rule #
    i = 0
    dst_len = len(splited_dst)
    while i < dst_len:
        if splited_dst[i] == '{':
            del splited_dst[i]
            a = splited_dst.pop(i)
            op = splited_dst.pop(i)
            b = splited_dst.pop(i)
            result = compute(a, op, b)

            if splited_dst[i] == '}': 
                splited_dst[i] = result
                dst_len -= 4
            else:
                splited_dst.insert(i, result)
                splited_dst.insert(i, '{')
                dst_len -= 2
                continue

        i += 1

    # Make a string from a list
    ret_str = str()
    for i in range(len(splited_dst)):
        if splited_dst[i] != '':
            ret_str += splited_dst[i] + ' '

    return ret_str.rstrip()

def compute(a, op, b):
    if op == '>>':
        return str(int(a) >> int(b))
    if op == '<<':
        return str(int(a) << int(b))
    if op == '&':
        return str(int(a) & int(b))
    if op == '+':
        return str(int(a) + int(b))
    if op == '-':
        return str(int(a) - int(b))
    if op == '%':
        return str(int(a) % int(b))
    if op == '*':
        return str(int(a) * int(b))
    if op == '/':
        return str(int(a) / int(b))
    if op == '==':
        return str(int(a) == int(b))
    if op == '!=':
        return str(int(a) != int(b))  
    
# Create pairs (variable : number)
def var_dictionary(splited_fact, splited_rule):
    
    var_dict = dict()
    correction = 0      # Offset for splited fact because of wildcards
    wildcard_i = 0      # Wildcard id
    for i in range(len(splited_rule)):
        if splited_rule[i][0] == '?':
            var_dict[ splited_rule[i][1] ] = splited_fact[i + correction].rstrip()
        
        # Wild card
        if splited_rule[i] == '...':
            val = str()
            for el in splited_fact[i + correction:]:
                if el == ']':
                    break
                val += el + ' '
                correction += 1

            var_dict[ '...' + str(wildcard_i) ] = val.rstrip()
            wildcard_i += 1
            correction -= 1

    return var_dict

def execute_rule(rule, fact):
    splited_fact = fact.rstrip().split(' ')

    rule_ = rule.split('\n')[0].split(',')[0][3:]
    splited_rule = rule_.rstrip().split(' ')

    # Create pairs (variable : number)
    var_dict = var_dictionary(splited_fact, splited_rule)

    then = list() 
    then += rule.split('\n')[1][5:].split(',')

    for action in then:
        if action.startswith('DELETE'):
            new_fact = action[7:-1]
            new_fact = vars_to_nums(var_dict, new_fact)
            delete(new_fact)      

        if action.startswith('ADD'):
            new_fact = action[4:-1]
            new_fact = vars_to_nums(var_dict, new_fact)
            add(new_fact)
            print("New fact \"" + new_fact +"\" added.")


## Deletes a fact from facts.txt ##
def delete(fact):

    with open("/home/kesler/Studing/UI/Zadanie4/facts.txt","r+") as facts:
        f = facts.readlines()
        facts.seek(0)
        deleted = False
        for line in f:
            if deleted or fact.rstrip() not in line.rstrip() :
                facts.write(line)
            else:
                deleted = True

        facts.truncate()

## Adds new fact to facts.txt ##
def add(fact):
    with open("/home/kesler/Studing/UI/Zadanie4/facts.txt","a") as facts:
        facts.write(fact.strip() + '\n')

# def add_into_wild_card(new_fact, splited_fact):
#     splited_new_fact = new_fact.split(' ')

#     i = 0
#     l = len(splited_new_fact)
#     while i < l:
#         if splited_new_fact[i] == '...':
#             splited_new_fact.pop(i)
#             l -= 1

#             j = i
#             while splited_fact[j-1] != '[':
#                 j -= 1

#             while splited_fact[j] != ']':
#                 splited_new_fact.insert(i, splited_fact[j])
#                 i += 1
#                 l += 1
#                 j += 1
#         i += 1

#     ret_str = str()
#     for i in range(len(splited_new_fact)):
#         ret_str += splited_new_fact[i] + ' '

#     return ret_str


start()