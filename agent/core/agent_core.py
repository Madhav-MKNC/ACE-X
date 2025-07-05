from core.consciousness_loop import ConsciousnessLoop
from core.identity import Identity
from core.self_model import SelfModel

class AgentCore:
    def __init__(self):
        self.identity = Identity()
        self.self_model = SelfModel(self.identity)
        self.consciousness = ConsciousnessLoop(self.identity, self.self_model)

    def run(self):
        print(f"👤 Booting agent: {self.identity.name}")
        self.consciousness.run_forever()
