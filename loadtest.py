import unittest
import xmlrunner
from testapi import TestApi

apitest = unittest.TestLoader().loadTestsFromTestCase(TestApi)
xmlrunner.XMLTestRunner(verbosity=2, output='test-reports').run(apitest)

