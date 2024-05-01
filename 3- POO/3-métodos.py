class Movie:
    def __init__(self,name,yearLaunch,includedPlan,note,durationMinutes):
        self.name = name
        self.yearLaunch = yearLaunch
        self.includedPlan = includedPlan
        self.note = note
        self.durationMinutes = durationMinutes

    #Retorna um valor específico
    def __str__(self):
         return f"Filme: {self.name}"
        
    #Métodos

    def technical_sheet(self):
        print("####Dados do Filme####")
        print(f"Nome Filme: {self.name}")
        print(f"Ano Lançamento: {self.yearLaunch}")
        print(f"Está no plano? {self.includedPlan}")
        print(f"Avaliação Filme: {self.note}")
        print(f"Duração Filme: {self.durationMinutes}")

movie = Movie("Super Mario", 2023, False, 10.0, 120)
movie.technical_sheet()
