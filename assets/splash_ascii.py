import threading
import time
from auth import get_current_user

class SplashScreen:
    def __init__(self, user_name: str):
        self.user_name = user_name
        self.ascii_mascote = """
      /\\_/\\
     ( o.o )
      > ^ <
    """
        self.animation_frame = 0
        self.animation_speed = 0.1

    def show(self):
        print(f"Starting splash screen for user: {self.user_name}")
        print(self.ascii_mascote)
        time.sleep(2)
        print("Splash screen finished.")
