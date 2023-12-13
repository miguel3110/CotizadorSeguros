from re import match

ONLY_FIRST = '^(?:PE|E|N|[23456789]|[23456789](?:A|P)?|1[0123]?|1[0123]?(?:A|P)?)$'
FIRST_AND_BOOK = '^(?:PE|E|N|[23456789]|[23456789](?:AV|PI)?|1[0123]?|1[0123]?(?:AV|PI)?)-?$'
BOOK_AND_TOME = '^(?:PE|E|N|[23456789](?:AV|PI)?|1[0123]?(?:AV|PI)?)-(?:\d{1,4})-?$'
FULL_ID = '^(PE|E|N|[23456789](?:AV|PI)?|1[0123]?(?:AV|PI)?)-(\d{1,4})-(\d{1,6})$'

FULL_VALID = '^P$|{}|{}|{}|{}'.format(ONLY_FIRST, FIRST_AND_BOOK, BOOK_AND_TOME, FULL_ID)
ONLY_VALID_ID = FULL_ID

LETTER = '^PE|E|N$'
NUMBER = '^(1[0123]?|[23456789])?$'
MIXED_ID = '^(1[0123]?|[23456789])(AV|PI)$'


def validate_id(id):
    """
    Accepted patterns:
    - Regular (provincia-libro-tomo). Ej: 1-1234-12345
    - Panameño nacido en el extranjero (PE-libro-tomo). Ej: PE-1234-12345
    - Extranjero con cédula (E-libro-tomo). Ej: E-1234-123456
    - Naturalizado (N-libro-tomo). Ej: N-1234-12345
    - Panameños nacidos antes de la vigencia (provinciaAV-libro-tomo). Ej: 1AV-1234-12345
    - Población indigena (provinciaPI-libro-tomo). Ej: 1PI-1234-12345

    Identificación de las provincias:
    - 1: Bocas del Toro
    - 2: Coclé
    - 3: Colón
    - 4: Chiriquí
    - 5: Darién
    - 6: Herrera
    - 7: Los Santos
    - 8: Panamá
    - 9: Veraguas
    - 10: Guna Yala
    - 11: Emberá Wounaan
    - 12: Ngäbe-Buglé
    - 13: Panamá Oeste
    :param id:
    :return: object
    {
        is_valid: True|False, # true if the string could be a valid id, useful while typing.
        input: str,    # Input value.

        is_complete: True|False,  # boolean that tells if it is a complete id.

        id: ["1","2","3","4"]       # Array with the separated components of the id (province, letters, book, volume).
                                    # null - if isValid == false.
                                    # [undefined, undefined, undefined, undefined] - if is_complete == False.
                                    # ["1","2","3","4"] - Values of the id if it is valida and complete (is_valid == is_complete == True).
    }
    """
    matched = match(FULL_VALID, id)

    is_complete = False

    groups = None
    if matched is not None:
        groups = list(matched.groups())

        #print('groups', groups)
        if groups[0] is not None:
            is_complete = True
            if match(LETTER, groups[0]) is not None:
                groups.insert(0, '0')
            if match(NUMBER, groups[0]) is not None:
                groups.insert(1, '')
            if match(MIXED_ID, groups[0]) is not None:
                tmp = match('(\d+)(\w+)', groups[0])
                groups.insert(0, tmp[1])
                groups.insert(1, tmp[2])
    return True if len(id) == 0 else matched is not None