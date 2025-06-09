class Eagle:
    def __init__(self, name, wingspan):
        self.name = name
        self.wingspan = wingspan

    def info(self):
        return f"독수리 이름: {self.name}, 날개 길이: {self.wingspan}cm"

    def family(self):
        return "매과"
