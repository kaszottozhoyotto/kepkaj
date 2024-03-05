
import re

class StringCalculator:
    def __init__(self, name, age):
      self.name = name
      self.age = age

    def Calculate(string):
      if(string == None):
        return 0

      delimiters = [',', '\n']

      #if(string.startswith('//')):


      output = re.findall("//
",string)
      for o in output:
        o.replace('/','')
        o.replace('[','')
        o.replace(']','')
        delimiters.append(o)

      string = string.replace('/','')
      string =string.replace('[','')
      string =string.replace(']','')

      for delimiter in delimiters:
        string = " ".join(string.split(delimiter))

      result = string.split()

      sum = 0
      for substring in result:
        if(int(substring)>1000):
          continue
        if(int(substring)<0):
          raise Exception("Sorry, no numbers below zero")
        sum += int(substring)

      return sum



     

def Test():
  calculator = StringCalculator

  assert calculator.Calculate(None) == 0

  assert calculator.Calculate('356') == 356

  assert calculator.Calculate('20,10') == 30

  assert calculator.Calculate('20\n30') == 50

  assert calculator.Calculate('30,50,10') == 90

  assert calculator.Calculate('30,50,10000') == 80

  assert calculator.Calculate('//[#]30,50#10XD10//[XD]') == 100


     

import unittest

class MyTestCase(unittest.TestCase):
    def test(self):
        with self.assertRaises(Exception) as context:
            StringCalculator.Calculate('-10,10,10')

        self.assertTrue('This is broken' in context.exception)

if __name__ == '__main__':
    print("Witamy ciebie użytkowniku!")
    Test()
    unittest.main()
