from getcharacter import GetCharacter

def test_sprt():
  gc = GetCharacter(0, 0, 0, 0)
  gc.add('hellokitty')
  gc.add('hangyodon')
  gc.add('hangyodon')
  result = gc .sort()
  assert result == 'hangyodon'

def test_sprt():
  gc = GetCharacter(0, 0, 0, 0)
  gc.add('hellokitty')
  gc.add('melody')
  gc.add('melody')
  result = gc .sort()
  assert result == 'melody'

def test_sprt():
  gc = GetCharacter(0, 0, 0, 0)
  gc.add('hangyodon')
  gc.add('hangyodon')
  gc.add('kuromi')
  result = gc .sort()
  assert result == 'hangyodon'

 