from dataclasses import dataclass, field, asdict
import tkinter.filedialog
import json
import copy


@dataclass
class Blueprint:
    """
    """
    version: int                  = field(init=False, default=4)
    bodies:  list['Body']         = field(init=False, default_factory=list)
    joints:  list['Joint'] | None = field(init=False, default=None)


    def print(self):
        print(json.dumps(asdict(self), indent=4))


    def save(self, path: str = '') -> bool:
        if not path:
            path = tkinter.filedialog.asksaveasfilename(
                title='save blueprint file', defaultextension='.json')
            if not path:
                return False
        with open(path, mode='w') as file:
            json.dump(asdict(self), file)
        return True


    def clone(self) -> 'Blueprint':
        bp = copy.deepcopy(self)

        # offset interactable controller id's
        from .interactable_parts.interactable_part import InteractablePart
        controllers = [c.controller for body in bp.bodies for c in body.childs 
                       if isinstance(c, InteractablePart)]
        min_id = min(controllers, key=lambda c: c.id).id
        max_id = max(controllers, key=lambda c: c.id).id
        id_diff = max_id - min_id
        for c in controllers:
            c.id += id_diff
            for target in c.controllers or []:
                target.id += id_diff
        InteractablePart.Controller.id += id_diff

        return bp
