class SelfModel:
    def __init__(self, identity):
        self.identity = identity
        self.abilities = {
            "perceive": True,
            "reason": True,
            "express": True,
            "reflect": True,
            "evolve": True,
        }
        self.memory_refs = []
        self.current_mood = "neutral"
        self.status = "idle"

    def update_state(self, mood=None, status=None):
        if mood: self.current_mood = mood
        if status: self.status = status

    def introspect(self):
        return {
            "name": self.identity.name,
            "mood": self.current_mood,
            "status": self.status,
            "abilities": self.abilities,
        }
