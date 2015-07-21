# -*- Mode:Python; indent-tabs-mode:nil; tab-width:4 -*-
#
# Copyright (C) 2015 Canonical Ltd
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 3 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from contextlib import contextmanager
import os
import tempfile
import unittest

import snapcraft.dirs


@contextmanager
def chdir(wd):
    cwd = os.getcwd()
    try:
        os.chdir(wd)
        yield
    finally:
        os.chdir(cwd)


class TestCase(unittest.TestCase):

    def setUp(self):
        super().setUp()
        snapcraft.dirs.setup_dirs()
        tempdirObj = tempfile.TemporaryDirectory()
        self.addCleanup(tempdirObj.cleanup)
        self.tempdir = tempdirObj.name
