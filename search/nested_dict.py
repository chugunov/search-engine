from collections import defaultdict


class NestedDict(defaultdict):
    def __init__(self):
        super().__init__(lambda: defaultdict(int))
