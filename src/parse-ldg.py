import smblueprint as sm
import smblueprint.util as util


bp = sm.Blueprint()
bd = sm.Body(bp)

in_positioner = util.Line((0,0,1), (-1,0,0))
gt_positioner = util.Line((0,1,1), (-1,0,0))
out_positioner = util.Line((0,2,1), (-1,0,0))

gate_dict = {}
def gate_from_str(s: str):
    global bd, gate_dict
    if s not in gate_dict:
        try:
            i = [c.isdigit() for c in s+'0'].index(True)    # remove numbering
            gate_dict[s] = sm.LogicGate(bd, 
                mode=sm.LogicGate.Mode[s[:i]], 
                pos=None,
                color=sm.Color.Logic_Gate)
        except KeyError:                                    # handle IN gates
            gate_dict[s] = sm.LogicGate(bd, 
                mode=sm.LogicGate.Mode.OR, 
                pos=in_positioner(),
                color=sm.Color.GREEN)

    return gate_dict[s]


with open("circuits/4bit_popcount.ldg") as file:
    content = file.read()

    # parse connections
    lines = content.split('\n')
    for line in lines:
        if line == '' or line.startswith('#'): 
            continue

        gate_groups = [[gate_from_str(word.strip()) 
                        for word in group.split(',')]
                        for group in line.split('->')]

        for src_gates, dst_gates in zip(gate_groups[:-1], gate_groups[1:]):
            for src in src_gates:
                src >> dst_gates

    # positioning cleanup
    for child in bd.childs:
        if isinstance(child, sm.LogicGate):
            if child.controller.controllers is None:
                child.pos = out_positioner()
                child.color = sm.Color.RED
            elif child.pos is None:
                child.pos = gt_positioner()

    bp.print()
