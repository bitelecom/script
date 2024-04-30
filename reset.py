import subprocess

def reset_windows():
    try:
        # Executar o comando do PowerShell para redefinir o Windows
        subprocess.run(["powershell", "-Command", "SystemReset -FactoryReset"], check=True)

        # Aqui você pode adicionar comandos adicionais para remover usuários específicos, se necessário.
        # Exemplo: subprocess.run(["powershell", "-Command", "Remove-LocalUser -Name 'NomeDoUsuario'"], check=True)

    except subprocess.CalledProcessError as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    reset_windows()
