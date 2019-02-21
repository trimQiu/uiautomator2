import uiautomator2 as u2
import unittest

class Case1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.d = u2.connect()
        cls.d.unlock();
        cls.d.set_orientation('natural')
        cls.d.implicitly_wait(10)