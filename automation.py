file = open("data_structure.txt", "r")
#get accepting state
for line in file:
    line = line.strip()
    end = line
    break

#get alphabet
alphabet = []
for line in file:
    if line == "\n":
        break
    line = line.strip()
    alphabet.append(line)

#get transitions
transitions = []
for line in file:
    line = line.strip()
    line = line.split()
    transitions.append(line)

#output array (needs to be formatted better)
output = []
def accept(inp):
    #current transition, initialize it to start transition
    curr = transitions[0][0]
    inp = inp.strip()
    inp = inp.split()
    for i in range(len(inp)):
        #see if input component in alphabet
        if inp[i] not in alphabet:
            print("Rejected, not in alphabet")
            return
        #find valid transition for input
        for j in range(len(transitions)):
            #if current state
            if transitions[j][0] == curr:
                #if state has a transition for the input
                if transitions[j][1] == inp[i]:
                    #add transition to output array
                    output.append(transitions[j])
                    #update current state, since moving to next state
                    curr = transitions[j][2]
                    break
            #if all transitions were looped through and no valid one was found
            if j == len(transitions)-1:
                #reject
                print("Rejected, no transition")
                print(output)
                return
    #If input successfully made it to accepting state
    if curr == end:
        #accept
        print("Accepted")
        print(output)
    else:
        #reject otherwise
        print("Rejected")

inp = input("Enter recipe here (separate each item with a space): ")
accept(inp)