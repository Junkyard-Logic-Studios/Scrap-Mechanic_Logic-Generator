import smblueprint as sm

bp = sm.Blueprint()
bd = sm.Body(bp)

block = sm.Block(bd, sm.ShapeID.Blocks.Spaceship, color=sm.Color.Spaceship_Block)
part = sm.Part(bd, sm.ShapeID.Parts.Baby_Duck_Statuette, color=sm.Color.YELLOW)
gate = sm.LogicGate(bd, sm.LogicGate.Mode.XOR)
timer = sm.Timer(bd, 1, 20)
sensor = sm.Sensor(bd, 20)

bp.print()
bp.save()
