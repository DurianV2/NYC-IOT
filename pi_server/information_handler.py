class information_handler_:

    def __init__(self):
        self.is_home = False
    # this information will come from the sync get request
        self.first_warning = False
        # bool that is set when danger score reaches threshold
        self.in_danger = False

    def reset(self):
        self.is_home = True
        self.in_danger = False
        self.first_warning = False

    def set_is_home(self, is_home):
        self.is_home = is_home

    def set_in_danger(self, in_danger):
        self.in_danger = in_danger

    def set_first_warning(self, first_warning):
        self.first_warning = first_warning

    def get_is_home(self):
        return self.is_home

    def get_in_danger(self):
        return self.in_danger

    def get_first_warning(self):
        return self.first_warning
