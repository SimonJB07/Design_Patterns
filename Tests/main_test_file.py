import unittest
import doctest
import os
import coverage

COV = coverage.coverage(
    branch=True,
    include='../*',
    omit=[
        '../Tests/*',
    ]
)
COV.start()


class MainTests:

    @staticmethod
    def doc_tests():
        doctest.testfile("model_doctest.txt", verbose=1)

    @staticmethod
    def unit_test():
        tests = unittest.TestLoader().discover('../Tests', pattern='*tests.py')
        result = unittest.TextTestRunner(verbosity=2).run(tests)
        if result.wasSuccessful():
            COV.stop()
            COV.save()
            print('Coverage Summary:')
            COV.report()
            basedir = os.path.abspath(os.path.dirname(__file__))
            covdir = os.path.join(basedir, '../Tests/coverage')
            COV.html_report(directory=covdir)
            print('HTML version: file://%s/index.html' % covdir)
            COV.erase()
            return 0
        return 1


