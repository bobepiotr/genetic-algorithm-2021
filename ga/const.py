import os

RIGHT = 0
LEFT = 1
UP = 2
DOWN = 3

DIR_PATH = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(DIR_PATH, "exercises")

ZAD_0 = os.path.join(PATH, "zad0.txt")
ZAD_1 = os.path.join(PATH, "zad1.txt")
ZAD_2 = os.path.join(PATH, "zad2.txt")
ZAD_3 = os.path.join(PATH, "zad3.txt")
ZAD_4 = os.path.join(PATH, "zad4.txt")
ZAD_A = os.path.join(PATH, "zadA.txt")

'''
Parametrom tym przypisano wagi wi odpowiadające ich znaczeniu, tak aby
najwyżej karane było umieszczanie ścieżek poza dozwolonym obszarem, kolejno
mniej – przecinanie się ścieżek, długość ścieżek i najmniej liczba segmentów
tworzących.
'''

INTERSECTION_WEIGHT = 50
LENGTH_WEIGHT = 1
STEPS_WEIGHT = 0.1
OUT_PATHS_WEIGHT = 100
OUT_PATHS_LENGTH_WEIGHT = 10

CROSSOVER_PROBABILITY = 0.7
MUTATION_PROBABILITY = 0.8

# default genetic algorithm parameters
DEFAULT_TOURNAMENT_SIZE = 10
DEFAULT_GENERATION_AMOUNT = 200
DEFAULT_GENERATION_SIZE = 100

# paths for output files from report generator
RESEARCH_DATA_DIR = os.path.join(DIR_PATH, "research")
RESEARCH_IMAGES = os.path.join(RESEARCH_DATA_DIR, "images")
RESEARCH_DATA = os.path.join(RESEARCH_DATA_DIR, "data")

# constant keywords for GA parameters
KW_GEN_SIZE = 'gen_size'
KW_TOUR_SIZE = 'tour_size'
KW_GEN_AMOUNT = 'gen_amount'

# const keywords for report_generator module
KW_EXAM_PARAM = "exam_param"
KW_FILENAME = "filename"
KW_BEST_SOL = "best_sol"
KW_WORST_SOL = "worst_sol"
KW_FITTING_LIST = 'fitting_list'
