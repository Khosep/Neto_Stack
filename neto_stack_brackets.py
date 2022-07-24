class Stack:
    """Стек - абстрактный тип данных, представляющий собой список элементов, организованных по принципу LIFO"""

    def __init__(self):
        self.values = []

    def isEmpty(self):
        """Проверка стека на пустоту. Метод возвращает True или False"""
        return self.values == []

    def push(self, element):
        """Добавляет новый элемент на вершину стека. Метод ничего не возвращает"""
        self.values.append(element)

    def pop(self):
        """Удаляет верхний элемент стека. Стек изменяется. Метод возвращает удаляемый верхний элемент стека"""
        if self.isEmpty():
            return None
        return self.values.pop()

    def peek(self):
        """Возвращает верхний элемент стека, но не удаляет его. Стек не меняется"""
        if self.isEmpty():
            return None
        return self.values[-1]

    def size(self):
        """Возвращает количество элементов в стеке"""
        return len(self.values)

    def __str__(self):
        return f'stack: bottom {self.values} top'


def check_balanced_bracket_sequence(bracket_sequence: str):
    """ Проверяет сбалансированность скобочной последовательности:
    открывающий символ имеет соответствующий ему закрывающий, и пары скобок правильно вложены друг в друга"""
    stack = Stack()
    for bracket in bracket_sequence:
        if bracket in '({[':
            stack.push(bracket)
        elif bracket in ')}]':
            if stack.isEmpty() or ord(bracket) - ord(stack.pop()) > 2:
                print('Несбалансированно')
                break
        else:
            print('Несбалансированно: не скобки вообще')
            break
    else:
        print('Сбалансированно' if stack.isEmpty() else 'Несбалансированно')


if __name__ == "__main__":
    check_balanced_bracket_sequence(input('Введите последовательность из скобок:\n'))
