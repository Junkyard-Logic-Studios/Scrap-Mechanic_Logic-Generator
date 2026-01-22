import smblueprint as sm
import smblueprint.util as util

bp = sm.Blueprint()
bd = sm.Body(bp)

sm.Block(bd, sm.ShapeID.Blocks.Spaceship, (4,4,1), pos=(-1,-1,-1))

sensor = sm.Sensor(bd, 10, pos=(-1,0,0))
switch = sm.Switch(bd, pos=(0,2,0))
gate = sm.LogicGate(bd, sm.LogicGate.Mode.XOR, pos=(-1,1,0))
sensor >> gate
switch >> gate

timer = sm.Timer(bd, 1, 20)
gate >> timer

positioner = util.Line((2,-1,0), (0,1,0))
timer >> [sm.Headlight(bd, pos=positioner()) for _ in range(4)]

bp.print()
bp.clone().print()
bp.save()
