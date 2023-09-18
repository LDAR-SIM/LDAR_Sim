# ------------------------------------------------------------------------------
# Program:     The LDAR Simulator (LDAR-Sim)
# File:        stdout_redirect.py
# Purpose:     Redirects std.out or similar streams
#
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the MIT License as published
# by the Free Software Foundation, version 3.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# MIT License for more details.

# You should have received a copy of the MIT License
# along with this program.  If not, see <https://opensource.org/licenses/MIT>.
#
# ------------------------------------------------------------------------------

import threading


class stdout_redirect:
    def __init__(self, redirects):
        '''
        constructor takes a redirect stream
        redirects = a list of file like objects to push to
        '''
        self.redirects = redirects
        return

    def write(self, text):
        '''
        text is the text to push to the stdout
        '''
        for w in self.redirects:
            try:
                with threading.Lock():
                    w.write(text)
            except ValueError:
                pass

        return

    def flush(self):
        '''
        flush method
        '''
        for w in self.redirects:
            try:
                w.flush()
            except ValueError:
                pass

        return
