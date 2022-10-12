text = 'ололодл абволдодл оролабв'

def dep(text):
    text = list(filter(lambda x: 'абв' not in x, text.split()))
    return ' '.join(text)

text = dep(text)
print(text)