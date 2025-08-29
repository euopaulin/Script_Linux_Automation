#!/usr/bin/env python3
import subprocess
import sys

def autom_sudoapt(command):
    try:
        # Executa o comando e captura a saída
        subprocess.run(command, check=True, text=True, shell=True)
        print(f"Comando '{command}' executado com sucesso.")
    except subprocess.CalledProcessError as e:
        # Se o comando falhar, exibe o erro
        print(f"Erro ao executar o comando '{command}': {e}", file=sys.stderr)
        sys.exit(1)

def main():
    print("Iniciando a atualização e o upgrade do sistema...")
    
    # Executa a atualização da lista de pacotes
    autom_sudoapt("sudo apt update")
    
    # Executa o upgrade dos pacotes.
    # O -y responde 'sim' a qualquer prompt de confirmação.
    autom_sudoapt("sudo apt upgrade -y")
    
    print("Atualização e upgrade concluídos!")

if __name__ == "__main__":
    main()