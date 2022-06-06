def recursive_characters(nums=None):
    if len(nums) == 0 or nums == None:
        return []
    
    result = []
    
    # Оптимизация: 
    # Ключи словаря строки, нет необходимости конвертировать str в int.
    # Значеня солваря массив из букв, насколько я помню по услловию не указывалось как можно хранить буквы, а таким способом не нужно перебирать строки для того чтобы доставть отдельнные буквы.
    characters = {
        "2":["a", "b","c"],
        "3":["d", "e", "f"],
        "4":["g", "h", "i"],
        "5":["j", "k", "l"],
        "6":["m", "n", "o"],
        "7":["p", "q", "r", "s"],
        "8":["t", "u", "v"],
        "9":["w", "x", "y", "z"]
    }
    
    # Базовое условие рекурсии для выхода 
    if len(nums) == 1:
        return characters[nums]

    chars = characters[nums[0]]
    
    # наше рекурсивное условие
    recursive_chars = recursive_characters(nums[1:])
    
    # Каждую букву от первой цифры мы будем соединяять с буквой следующей цифры из рекрсивного вызова нашей функции
    for char in chars: 
        for recursive_char in recursive_chars:
            result.append(char + recursive_char)
    return result

assert recursive_characters("23") == ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']