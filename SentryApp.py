from raven import Client #pip install raven --upgrade
from Excepcional import ArremessadorDeExcecoes
from Hush import sentry_DSN

if __name__ == '__main__':
   #Cliente do Sentry
   client = Client(sentry_DSN)
   
   a = ArremessadorDeExcecoes() #Instancio sem o client - ele captura o erro automaticamente
   a.jogaExcecaoAleatoria()