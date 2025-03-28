class GetCharacter:
    def __init__(self, hello_kitty: int, melody: int, hangyodon: int, kuromi: int):
        self.apple_home ={
            'hello_kitty': hello_kitty,
            'melody': melody,
            'hangyodon': hangyodon,
            'kuromi': kuromi
        }


    def add(self, apple_home: str) -> None:
        if apple_home == 'hellokitty':
            self.apple_home['hellokitty'] = self.apple_home.get('hellokitty') + 1
        if apple_home == 'melody':
            self.apple_home['melody'] = self.apple_home.get('melody') + 1
        if apple_home == 'hangyodon':
            self.apple_home['hangyodon'] = self.apple_home.get('hangyodon') + 1
        if apple_home == 'kuromi':
            self.apple_home['kuromi'] = self.apple_home.get('kuromi') + 1

    def sort(self) -> str:
        score = 0
        result = ''

        for character, points in self.apple_home.items():
            if points > score:
                score = points
                result = character

        return result

    def clear(self) -> None:
        self.apple_home = {
            'hellokitty': 0,
            'melody': 0,
            'hangyodon': 0,
            'kuromi': 0
        }
    