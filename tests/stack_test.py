import sys
import os

# Добавляем путь к корневой директории проекта
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from stack.stack import Stack

def test_stack():
    """Тест функций стека"""
    s = Stack()
    s.push(3)
    assert s.peek() == 3

    s.push(2)
    s.push(1)

    assert s.__len__() == 3

    s.pop()
    assert s.peek() == 2

    assert s.min() == 2
    s.pop()
    s.pop()

    assert s.is_empty()


