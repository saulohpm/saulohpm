class Saulo:
    def __init__(self):
        self.role = "Mathematics, Programming, and Mechanical Engineering student"
        self.background = "Mechanical Engineering"

        self.interests = [
            "mathematical modeling",
            "numerical methods & computational simulation",
            "data analysis & data science",
            "software & systems development",
        ]

        self.education = [
            "M.Sc. (in progress) - Mechanical Engineering",
            "Technologist (in progress) - Systems Analysis & Development",
            "Postgrad - Financial Administration",
            "B.Ed. - Mathematics",
        ]

        self.projects = [
            "numerical-methods",
            "simulador-cdi",
            "analise-carteira-investimentos",
            "introducao-edo",
        ]

        self.stack = ["Python", "JavaScript", "LaTeX", "HTML", "CSS"]

    def build(self, problem):
        return f"a computational tool for: {problem}"


>>> Saulo().build("engineering problem")
'a computational tool for: engineering problem'
