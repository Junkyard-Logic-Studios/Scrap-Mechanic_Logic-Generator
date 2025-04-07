from dataclasses import dataclass, field, asdict
import tkinter.filedialog
import json


@dataclass
class Blueprint:
    """
    """
    version: int                  = field(init=False, default=4)
    bodies:  list['Body']         = field(init=False, default_factory=list)
    joints:  list['Joint'] | None = field(init=False, default=None)

    def print(self):
        print(json.dumps(asdict(self), indent=4))

    def save(self, path: str = ''):
        if not path:
            path = tkinter.filedialog.asksaveasfilename(
                title='save blueprint file', defaultextension='.json')
            if not path:
                return False
        with open(path, mode='w') as file:
            json.dump(asdict(self), file)
        return True
