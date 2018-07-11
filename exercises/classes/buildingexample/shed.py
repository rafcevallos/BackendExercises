from building import Building

class Shed(Building):
    """
    Author: Steve Brownlee

    Inherits from: Building

    Purpose: To represent any kind of shed for users to build in the UI

    """

    def __init__(self, windows):
        """
        Initialization method for Shed

        Arguments:
            windows {number} -- Integer for number of windows on the shed
            Building {[type]} -- [description]
        """
        super().__init__()
        self.windows = windows # this is a positional argument
        self.workbench = True
        self.tools = []
