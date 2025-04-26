class ReflexVacuumAgent:
    def __init__(self):
        self.location = "A"

    def perceive(self, environment):
        return environment[self.location]

    def decide(self, perception):
        if perception == "Dirty":
            return "Clean"
        else:
            return "Move"

    def act(self, action):
        if action == "Clean":
            print(f"Cleaning {self.location}")
        elif self.location == "A":
            self.location = "B"
        else:
            self.location = "A"

    def run(self, environment, steps=4):
        for _ in range(steps):
            perception = self.perceive(environment)
            action = self.decide(perception)
            self.act(action)
            if action == "Clean":
                environment[self.location] = "Clean"

# Environment setup: Room A is Dirty, Room B is Clean
environment = {"A": "Dirty", "B": "Clean"}

agent = ReflexVacuumAgent()
agent.run(environment)

# class ReflexVacuumAgent:
#     def __init__(self):
#         self.location = "A"

#     def perceive(self, environment):
#         return environment[self.location]

#     def decide(self, perception):
#         if perception == "Dirty":
#             return "Clean"
#         else:
#             return "Move"

#     def act(self, action):
#         if action == "Clean":
#             print(f"Cleaning {self.location}")
#         elif self.location == "A":
#             self.location = "B"
#         else:
#             self.location = "A"

#     def run(self, environment, steps=4):
#         for _ in range(steps):
#             perception = self.perceive(environment)
#             action = self.decide(perception)
#             self.act(action)
#             if action == "Clean":
#                 environment[self.location] = "Clean"

# # Environment setup: Room A is Dirty, Room B is Clean
# environment = {"A": "Dirty", "B": "Clean"}

# agent = ReflexVacuumAgent()
# agent.run(environment)
