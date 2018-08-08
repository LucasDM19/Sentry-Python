
class ArremessadorDeExcecoes():
   def __init__(self, _client=None):
      self.client = _client
      self.dic_Excecoes = {
         "ZeroDivisionError" : ['1 / 0'],
         "ModuleNotFoundError" : ["import ModuloInexistente"],
         "NameError" : ["resultado = 4 + variavelInexistente"],
         "TypeError" : ["variavelString = '2'", "variavelInteger = 2", "resultado = variavelString + variavelInteger"],
         "ValueError" : ["x = int('literal invalido para int')"],
         "FileNotFoundError" : ["f = open('ArquivoInexistente.txt', 'r')"],
         "AttributeError" : ["x = int.funcaoInexistente()"],
         "ImportError" : ["from sys import ModuloInexistente"],
         "IndexError" : ["lista = [1, 2]", "x = lista[12]"],
         "SyntaxError" : ["variavelSemValor = "],
         
      }
      
   def capturaExcecao(self):
      if self.client is not None:
         self.client.captureException()
   
   def jogaExcecao(self, tipoException):
      try:
         comandos = self.dic_Excecoes[tipoException]
         for comando in comandos:
            exec(comando)
      except Exception as ex:
         self.capturaExcecao()
         raise
   
   def jogaExcecaoAleatoria(self):
      import random
      tipoExcecao = random.choice([chave for chave in self.dic_Excecoes])
      self.jogaExcecao(tipoExcecao)
         
if __name__ == '__main__':
   a = ArremessadorDeExcecoes()
   a.jogaExcecao("SyntaxError")
   #a.jogaExcecaoAleatoria()
      