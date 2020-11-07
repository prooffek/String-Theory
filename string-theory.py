def is_palindrome(text):
    """
    >>> is_palindrome('Mr. Owl ate my metal worm')
    True
    >>> is_palindrome('Eva, can I see bees in a cave?')
    True
    """
    
    version_1 = ''.join([char for char in text.lower() if char.isalpha()])
    version_2 = ''.join(reversed(version_1))

    if version_1 == version_2:
        return True
    else:
        return False


def is_isogram(text):
    """
    >>> is_isogram('uncopyrightables')
    True
    """

    text_1 = ''.join([char for char in text.lower() if char.isalpha()])

    value = True
    
    for i in text_1:
        count = text_1.count(i)
        if count > 1:
            value = False
            break
        else:
            continue

    return value

def is_pangram(text):
    """
    >>> is_pangram('The quick brown fox jumps over the lazy dog')
    True
    """
    text = ''.join([char for char in text.lower() if char.isalpha()])
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "w", "v", "x", "y", "z"]
    value = True

    for i in alphabet:
        if i not in text:
            value = False
            break
        else:
            continue
    
    return value

def is_anagram(text1, text2):
    """
    >>> is_anagram('Justin Timberlake', "I'm a jerk but listen")
    True
    """
    text_1 = ''.join([char for char in text1.lower() if char.isalpha()])
    text_2 = ''.join([char for char in text2.lower() if char.isalpha()])
    value = True

    for element in text_1:
        if text_1.count(element) != text_2.count(element):
            value = False
            break
        else:
            continue
    
    for element in text_2:
        if text_1.count(element) != text_2.count(element):
            value = False
            break
        else:
            continue
    
    return value

def is_blanagram(text1, text2):
    """
    >>> is_blanagram('Justin Timberlake', "I'm a berk but listen")
    True
    """
    text_1 = ''.join([char for char in text1.lower() if char.isalpha()])
    text_2 = ''.join([char for char in text2.lower() if char.isalpha()])

    lista_1 = []

    for element in text_1:
        if text_1.count(element) == text_2.count(element):
            continue
        else:
            lista_1.append(element)
    
    if len(lista_1) == 2:
        return True
    else:
        return False




print(is_blanagram('Justin Timberlake', "I'm a berk but listen"))
print(is_blanagram('My little pony!', 'your ponny is little'))