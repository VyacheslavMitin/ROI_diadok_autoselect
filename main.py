# Модуль выделения строк в 1С Диадок для отправки

# Импорты
import time
import pyautogui as pg

# Переменные
RANGE = 100  # количество раз прожатия пробела
TIMEOUT = 0.5  # пауза между прожатиями
TIMEOUT_SWITCH = 3  # пауза ожидания переключения на 1С

print(f"Необходимо переключиться в 1С в течение {TIMEOUT_SWITCH} секунд")
time.sleep(TIMEOUT_SWITCH)  # ожидание

pg.press('left', presses=10)  # выбор крайнего левого столбца
pg.press('space')  # поставить галочку
time.sleep(TIMEOUT)  # подождать пока 1С поймет что галка появилась

for i in range (RANGE):
    pg.press('down')  # спуск на стркоу ниже
    time.sleep(TIMEOUT)
    pg.press('space')
    time.sleep(TIMEOUT)

pg.alert("Завершено", "Завершено")  # окно об окончании