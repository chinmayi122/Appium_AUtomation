#1.import the files
import unittest
from tests.LoginTest import LoginTest
from tests.CrudOperations_Test import CrudOperations_Test

#2.Create the object of the class using unitTest
cf=unittest.TestLoader().loadTestsFromTestCase(LoginTest)
gt=unittest.TestLoader().loadTestsFromTestCase(CrudOperations_Test)

#3.Create TestSuite
regressionTest=unittest.TestSuite([cf,gt])

#4.Call the Test Runner Method
unittest.TextTestRunner(verbosity=1).run(regressionTest)

