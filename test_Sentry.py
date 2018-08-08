#coding=utf-8
import unittest
from Excepcional import * #Classe a ser testada - Chama TUDO

def main():
    unittest.main()  

class TestExcepcional(unittest.TestCase):
   def __init__(self, *args, **kwargs):
      super(TestExcepcional, self).__init__(*args, **kwargs)
      self.a = ArremessadorDeExcecoes()
      
   def testZeroDivisionError(self):
      self.assertRaises(ZeroDivisionError, self.a.jogaExcecao, "ZeroDivisionError")

   def testModuleNotFoundError(self):
      self.assertRaises(ModuleNotFoundError, self.a.jogaExcecao, "ModuleNotFoundError")
    
   def testNameError(self):
      self.assertRaises(NameError, self.a.jogaExcecao, "NameError")
      
   def testTypeError(self):
      self.assertRaises(TypeError, self.a.jogaExcecao, "TypeError")
   
   def testValueError(self):
      self.assertRaises(ValueError, self.a.jogaExcecao, "ValueError")
      
   def testFileNotFoundError(self):
      self.assertRaises(FileNotFoundError, self.a.jogaExcecao, "FileNotFoundError")
      
   def testAttributeError(self):
      self.assertRaises(AttributeError, self.a.jogaExcecao, "AttributeError")
   
   def testImportError(self):
      self.assertRaises(ImportError, self.a.jogaExcecao, "ImportError")
      
   def testIndexError(self):
      self.assertRaises(IndexError, self.a.jogaExcecao, "IndexError")
      
   def testSyntaxError(self):
      self.assertRaises(SyntaxError, self.a.jogaExcecao, "SyntaxError")
      
if __name__ == '__main__':
    main()