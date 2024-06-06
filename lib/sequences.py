class MyString:
  def __init__(self, value =''):
     if not isinstance (value,str):
        raise ValueError("value must be a string")
     self.value = value

     def is_sentence(value):
        return self.value.endswith('.')
     print(is_sentence())

     def is_question(value):
        return self.value.endswith('?')
     print(is_question())

     def is_exclamation(value):
        return self.value.endswith('!')
     print(is_exclamation())

     def count_sentences(self):
        sentences = self.value.replace('?', '.').replace('!', '.').split('.')
        return len([sentence for sentence in sentences if sentence.strip()])
     print(count_sentences())

  def print_fibonacci(length):
    if length == 0:
        return []
    elif length == 1:
        return [0]
    elif length == 2:
        return [0, 1]
    else:
        first, second = 0, 1
        fib_sequence = []
        for i in range(length):
            fib_sequence.append(first)
            first, second = second, first + second
        return fib_sequence


  print(print_fibonacci(10))