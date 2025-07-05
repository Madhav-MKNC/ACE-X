import time
from datetime import datetime

class ConsciousnessLoop:
    def __init__(self, identity, self_model):
        self.identity = identity
        self.self_model = self_model
        self.tick = 0
        self.alive = True

    def run_forever(self):
        while self.alive:
            self.tick += 1
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"[{now}] Tick {self.tick} — Status: {self.self_model.status}")
            self.think()
            time.sleep(3)

    def think(self):
        self.self_model.update_state(status="thinking")
        summary = self.self_model.introspect()
        print(f"> Introspection: {summary}")
        self.self_model.update_state(status="idle")
