# 🐧 Script para automação da atualização do Linux

## Esse script tem como objetivo automatizar o sudo apt update && sudo apt upgrade

### Foi utilizado o 🐍 Python como linguagem do script

### Após criar o script você deve salvar o arquivo .py em algum lugar acessivel e depois criar um arquivo txt onde deverá colocar o seguinte comando:

```bash
[Desktop Entry]
Name=Atualizar Sistema
Comment=Executa a atualização e o upgrade do sistema
Exec=gnome-terminal -e "bash -c 'sudo python3 /home/seu_user/Documents/Script_Linux_Automation/script.py; read -p \"Pressione Enter para fechar...\";'"
Icon=utilities-terminal
Terminal=false
Type=Application
```
### Depois salve com .desktop e execute o comando.