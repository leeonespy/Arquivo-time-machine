from datetime import datetime, timedelta
from cores import Cores as C
import os, shutil, sys, time

class Sistema:
    def __init__(self):
        print(C.amarelo_claro + "\nORGANIZADOR DE ARQUIVO DO (MAIS RECENTE AO MAIS ANTIGO)" + C.resetar)
        self.pasta = input("Digite o caminho ou a localização dos ficheiros (Ex:c:/Users/win11/Documents/python/Arquivo time machine/livros importantes): ")
        self.data_actual = datetime.now()
        self.files = os.listdir(self.pasta)
        
        for i in self.files:
            self.movedor_arquivo((f"{self.pasta}/{i}"), datetime.fromtimestamp(int(os.path.getmtime(f"{self.pasta}/{i}"))))
        self.barra_progresso()

    def movedor_arquivo(self, origem, tempo):
        diferenca = self.data_actual - tempo
        
        if diferenca.days >= 30:
            if os.path.exists(f"{self.pasta}/livros antigos") == True:
                pass
            else:
                os.mkdir(f"{self.pasta}/livros antigos")
            if os.path.isfile(origem):
                shutil.move(origem, (f"{self.pasta}/livros antigos"))
        else:
            if os.path.exists(f"{self.pasta}/livros recentes") == True:
                pass
            else:
                os.mkdir(f"{self.pasta}/livros recentes")
            if os.path.isfile(origem):
                shutil.move(origem, (f"{self.pasta}/livros recentes"))

    

    def barra_progresso(self):
        for i in range(20):
            time.sleep(0.05)
            sys.stdout.write(C.negrito + C.vermelho + f"\rMovendo ficheiros:" + "." * (i % 4) + C.resetar)
            sys.stdout.flush
    
def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    try:
        limpar()
        Sistema()
    except (FileExistsError, FileNotFoundError, OSError, ValueError):
        print(C.negrito + C.vermelho_claro + "ERROR: Caminho invalido ou Ficheiros não encontrados!", C.verde_claro + "Tente novamente" + C.resetar)
        time.sleep(3)
