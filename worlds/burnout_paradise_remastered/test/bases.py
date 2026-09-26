from test.bases import WorldTestBase
from .. import BURNOUT_PARADISE_REMASTERED

import unittest
unittest.TestCase.maxDiff = None

class BurnoutParadiseRemasteredTestBase(WorldTestBase):
    game = BURNOUT_PARADISE_REMASTERED
    maxDiff = None
