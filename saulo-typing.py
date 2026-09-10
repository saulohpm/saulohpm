class Saulo:
    def __init__(self):
        self.role = "Student and Researcher"
        self.background = "Mathematics, Programming, and Mechanical Engineering"

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

        self.stack = ["Python", "JavaScript", "LaTeX", "HTML", "CSS"]


    def build(self, problem):
        return f"a computational tool for: {problem}"


>>> Saulo().build("math problem")
'a computational tool for: math problem'
>>> print("Check out the repositories and projects below")
Check out the repositories and projects below'
