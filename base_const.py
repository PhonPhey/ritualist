'''Header file with base const'''

WIN_TITLE = "Ritualist"
WIN_WIDTH = 475  # Ширина создаваемого окна
WIN_HEIGHT = 600  # Высота
# Группируем ширину и высоту окна в одну переменную
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
WIN_BACKGROUND_COLOR = (27, 54, 20)
PLATFORM_WIDTH = 40
PLATFORM_HEIGHT = 40
# Группируем ширину и высоту платформы в список
PLATFORM = (PLATFORM_WIDTH, PLATFORM_HEIGHT)
PLATFORM_COLOR = (255, 98, 98)
MOVE_SPEED = 7
WIDTH = 32
HEIGHT = 32
# Группируем ширину и высоту спрайта в список
SPRITE = (WIDTH, HEIGHT)
COLOR = "#888888"
COLL_OBS = ["*", "-", "_", "A"]  # Коллекция припятствий

# Масштаб для стен
TEXTURE_WALL_WIDTH_SCALE = 0.08
TEXTURE_WALL_HEIGHT_SCALE = 0.07

# Масштаб для пола и припятствий
TEXTURE_FLOOR_WIDTH_SCALE = 0.09
TEXTURE_FLOOR_HEIGHT_SCALE = 0.07


