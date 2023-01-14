categories_tasks = [
    {'title': 'Криптография задания', 'options': [
        'криптография', 'крипта', 'криптопротокол', 'crypto', 'cryptography']},
    {'title': 'Реверс задания', 'options': [
        'реверс', 'ревёрс', 'обратный разработка', 'реверс инжиниринг', 'reverse']}
    {'title': 'Веб задания', 'options': ['веб', 'web', 'http', 'cors', 'csrf']}
    {'title': 'SQL задания', 'options': [
        'sql', 'инъекция', 'sql-инъекция', 'sql injection', 'sql injections']},
    {'title': 'XSS задания', 'options': [
        'xss', 'xxs', 'cross-site scripting', 'cross site scripting']},
    {'title': 'Стеганография задания', 'options': [
        'стеганография', 'stego', 'steganography', 'стенография']},
    {'title': 'Forensic задания', 'options': [
        'форенсик', 'forensic', 'криминалистика', 'компьютерный криминалистика']},
]

categories_definitions = [
    'CTF определение',
]


def generate_data_for_category(file, tasks=True):
    task_synonymous = ['задание', 'таск', 'тренировка', 'тренировать']
    prepositions = ['по', 'на', 'с', '']
    
