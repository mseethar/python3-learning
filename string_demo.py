my_text = '''Return a copy of the string where all tab characters are replaced by one or more spaces, depending on the current column and the given tab size. Tab positions occur every tabsize characters (default is 8, giving tab positions at columns 0, 8, 16 and so on). To expand the string, the current column is set to zero and the string is examined character by character. If the character is a tab (\t), one or more space characters are inserted in the result until the current column is equal to the next tab position. (The tab character itself is not copied.) If the character is a newline (\n) or return (\r), it is copied and the current column is reset to zero. Any other character is copied unchanged and the current column is incremented by one regardless of how the character is represented when printed.'''

print(my_text)

print('Number of ands', my_text.count('and'))

txt1 = '{0} is greater {word} than {1}, {phrase}'

print(txt1.format(2, 1, **{'phrase': 'oh, my!', 'word': 'sure'})) # Positional and keyword formatting can be mixed

print('abcdefghijklmnopqrstABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'.isalnum())
print('12.3'.isalnum())

txt2 = '   one two       '
print('"'+txt2.rstrip()+'"')
print(txt2.title())
