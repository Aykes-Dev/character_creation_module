from random import randint

# Global variable
DEFAULT_ATTACK = 5
DEFAULT_DEFENCE = 10


class Character:
    """Parent class of invisible front fighters."""
    RANGE_VALUE_ATTACK = (1, 3)
    RANGE_VALUE_DEFENCE = (1, 5)
    SPECIAL_BUFF = 15
    SPECIAL_SKILL = 'Удача'
    BRIEF_DESC_CHAR_CLASS = 'отважный любитель приключений'

    def __init__(self, name: str) -> None:
        self.name = name

    def attack(self) -> str:
        """Attack. Return random damage."""
        value_attack: int = DEFAULT_ATTACK + randint(*self.RANGE_VALUE_ATTACK)
        return (f'{self.name} нанёс противнику урон, равный {value_attack}')

    def defence(self) -> str:
        """Defence. Return random block."""
        value_defence: int = (
            DEFAULT_DEFENCE + randint(*self.RANGE_VALUE_DEFENCE))
        return (f'{self.name} блокировал {value_defence} ед. урона.')

    def special(self):
        """Special. Return magic attack."""
        return (f'{self.name} применил специальное умение '
                f'"{self.SPECIAL_SKILL} {self.SPECIAL_BUFF}".')

    def __str__(self) -> str:
        """Return class description."""
        return f'{self.__class__.__name__} - {self.BRIEF_DESC_CHAR_CLASS}'


class Warrior(Character):
    """Class Warrior"""
    def __init__(self) -> None:
        super().__init__()


class Mage(Character):
    """Class Mage"""
    def __init__(self) -> None:
        super().__init__()


class Healer(Character):
    """Class Healer"""
    def __init__(self) -> None:
        super().__init__()
