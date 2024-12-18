
# Playlist
# Ranepa case for playlist task
# Представим, что некое приложение хранит плейлист песен в двух видах:
#   * список списков с парами значений строка-вещественное число
#   * кортеж строк
# Каждая песня содержит: название и время звучания.

# Задание
# 1. Посчитайте общее время звучания n случайных песен, где n - количество запрошенных песен
# 2. Используйте модули random и datetime. Или любые другие.
# 3. Решение должно включать функцию, которая в качестве аргумента способна принимать плейлисты разных типов данных

# В результате решением задачи является функция, которая:
#   * может принимать как первый плейлист, так и второй в качестве аргумента
#   * принимает параметр n, число. Это количество песен
#   * возвращает время звучания, как объект времени timedelta, либо строку, либо вещественное число
# При этом функций в задаче может быть несколько. То есть решение можно разбить на несколько функций.
# Но результат задачи можно получить вызвав одну функцию!
# get_duration(playlist: Iterable, n: int) -> Any

playlist_a = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ["Staying' Alive", 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]

playlist_c = (
    "Happy Nation; 3.32",
    "It's My Life; 3.59",
    "Lady (Hear Me Tonight); 5.07",
    "Fields Of Gold; 3.38",
    "The Winner Takes It All; 4.54",
    "Self Control; 4.06",
    "I Shot The Sheriff; 4.57",
    "Don't Give Up; 6.34",
    "Relax, Take It Easy; 4.30",
    "Dancing Queen; 3.36",
)














import random 
from datetime import timedelta

def parse_playlist_c(playlist):
    parsed_playlist = []
    for song in playlist:
        title, duration = song.rsplit(';', 1)
        parsed_playlist.append([title.strip(), float(duration.strip())])
    return parsed_playlist 

def get_random_songs(playlist, n):
	return random.sample(playlist, n)	
	
def calculate_total_duration(songs):
    total_duration = sum(song[1] for song in songs)
    return total_duration

def convert_to_timedelta(total_duration):
	return timedelta(minutes=total_duration)
	
def format_duration(td):
    total_seconds = int(td.total_seconds())
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    return f"{minutes:02}:{seconds:02}" 	
	
def get_duration(playlist, n):
    if isinstance(playlist[0], str):
      playlist = parse_playlist_c(playlist)
      
    random_songs = get_random_songs(playlist, n) 	
    total_duration = calculate_total_duration(random_songs)
    
    return format_duration(convert_to_timedelta(total_duration))

print(get_duration(playlist_a, 3))
print(get_duration(playlist_c, 4)) 