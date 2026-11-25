import threading
import time
from auth import get_current_user

class SplashScreen:
    def __init__(self, user_name: str):
        self.user_name = user_name
        self.duration = 2.0  # segundos de duração
        self.ascii_mascote = """
      /\\_/\\
     ( o.o )
      > ^ <
    """

    def show(self):
        print(self.ascii_mascote)
        print(f"Splash Screen: Olá {self.user_name}")
        time.sleep(self.duration)
        # Aqui você pode redirecionar para a tela principal ou iniciar o fluxo principal
        # self.redirect_to_main()

# Exemplo de uso em Main.py (dentro de handle_client_thread):
# splash = SplashScreen(user_data.get('name', 'Usuário'))
# splash.show()
