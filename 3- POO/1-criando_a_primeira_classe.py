class Movie:
    name = ''
    yearLaunch = 0
    includedPlan = False
    note = 0
    durationMinutes = 0

# Primeiro Filme

movie = Movie()
movie.name = 'Xógum A Gloriosa Saga do Japão'
movie.yearLaunch = 2024
movie.includedPlan = False
movie.note = 8.9
movie.durationMinutes = 200
print('#Dados do filme#')
print(f'Nome da Série: {movie.name} \nAno de Lançamento: {movie.yearLaunch} \nNota: {movie.note}')