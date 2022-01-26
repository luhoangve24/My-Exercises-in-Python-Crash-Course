from http.client import responses
import unittest
import Counts

""" file_path = 'P10_FileAndEx\\ProjectGutenberg.txt'

class CountTestCase(unittest.TestCase):
    '''Test for "Counts.py" '''

    def test_count_text(self):
        '''Does it work?'''
        counts = Counts.count_words(file_path)
        self.assertEqual(counts, 1160)

if __name__ == '__main__':
    unittest.main() """

import location

""" class TestCaseLocation(unittest.TestCase):
    '''Test for formatted string location'''
    def test_string_location(self):
        loca = location.location('Ha Noi', 'Viet Nam')
        self.assertEqual(loca, 'Ha Noi, Viet Nam') 
    
if __name__ == '__main__':
    unittest.main() """

import sys
sys.path.append("E:\\Lab\\LaptrinhPython\\P11_TestCase")
import Survey

""" class TestAnonymousSurvey(unittest.TestCase):
    def test_store_single_respone(self):
        '''Test 1 response'''
        question = '''Ferrari or Lamborghini ?'''
        my_question = Survey.AnonymousSurvey(question)
        my_question.store_results('Ferrari please')
        self.assertIn('Ferrari please', my_question.responses)

    def test_store_three_respin(self):
        '''Test 3 responses'''
        question = '''What language are your favorite languages?'''
        my_question = Survey.AnonymousSurvey(question)
        responses = ['C++', 'C Sharp', 'HTML', 'CSS', 'JavaScripts']
        for respone in responses:
            my_question.store_results(respone)

        for respone in responses:
            self.assertIn(respone, responses)
        
if __name__ == '__main__':
    unittest.main() """

class TestAnonymousSurvey(unittest.TestCase):
    def setUp(self):
        '''Create a survey and set of responses for use in
        all test methods.'''
        question = '''
            What programming language are 
            your favorite languages?'''
        self.my_survey = Survey.AnonymousSurvey(question)
        self.responses = [
                'C++', 'C Sharp', 'HTML', 
                'CSS', 'JavaScripts']
    
    def test_store_single_response(self):
        self.my_survey.store_results(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        for response in self.responses:
            self.my_survey.store_results(response)
        
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

if __name__ == '__main__':
    unittest.main()