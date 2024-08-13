class Course():
    def __init__(self, skills: list = []):
        self.skills = skills

    def IdentifyMinSkillDeltaForDuel(self):
        delta = 500000
        skill_before = 0
        for skill in self.skills:
            delta_temp = skill - skill_before
            if delta_temp < delta:
                delta = delta_temp
        return delta

class Horse():
    def __init__(self, puissance: int):
        self.puissance = puissance
    
    @staticmethod
    def GetHorseInfos() -> int:
        return int(input())

# We get the numbers of horses
nb_horses = int(input())
horses = []

# We get all the horses infos and stock them into the horses list
for horse in range(nb_horses):
    horse_infos = Horse.GetHorseInfos()
    horses.append(Horse(horse_infos))

print(horses, file=sys.stderr, flush=True)

course_horses = Course(horses.sort(reverse=True))
delta_min = course_horses.IdentifyMinSkillDeltaForDuel()

print(delta_min)