if __name__ == "__main__":
    class ExamplePrint:
        def __init__(self):
            name = input("Wha`s your name? ").strip().title()
            self.name = name
        
        def display(self):
            return f"Hello {self.name}" 
            #print( "Hello", "how are you?", sep="---", end="Fuck") 

    objExamplePrint = ExamplePrint()
    print(objExamplePrint.display())