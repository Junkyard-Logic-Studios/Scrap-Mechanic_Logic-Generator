import smblueprint as sm
import smblueprint.util as util

bp = sm.Blueprint()
bd = sm.Body(bp)

gate_dict = {}
positioner = util.Line((0,0,0), (1,0,0))
def gate_from_str(s):
    global bd, gate_dict
    if s not in gate_dict:
        try:
            try:
                i = [c.isdigit() for c in s].index(True)
            except ValueError:
                i = len(s)
            mode = sm.LogicGate.Mode[s[:i]]     # remove numbering
        except KeyError:
            mode = sm.LogicGate.Mode.OR         # handle IN gates
        gate_dict[s] = sm.LogicGate(bd, mode, pos=positioner())
    return gate_dict[s]

with open("circuits/rising_edge_tick.ldg") as file:
    content = file.read()
    lines = content.split('\n')[:-1]
    for line in lines:
        gate_groups = [[gate_from_str(word.strip()) 
                        for word in group.split(',')]
                        for group in line.split('->')]
        for src_gates, dst_gates in zip(gate_groups[:-1], gate_groups[1:]):
            for src in src_gates:
                src >> dst_gates
    
    bp.print()
