class Intern:
    def __init__(self, name="My name? I’m nobody, an intern, I have no name."):
        self.name = name
    
    def __str__(self):
        return self.name
    
    def work(self):
        raise Exception("I’m just an intern, I can’t do that...")
    
    def make_coffee(self):
        return Coffee()

class Coffee:
    def __str__(self):
        return "This is the worst coffee you ever tasted."

# Testing the Intern class
if __name__ == "__main__":
    intern_default = Intern()
    intern_mark = Intern("Mark")
    
    print(intern_default)
    print(intern_mark)
    
    marks_coffee = intern_mark.make_coffee()
    print(marks_coffee)
    
    try:
        intern_default.work()
    except Exception as e:
        print(e)

