from Zadanie2Lista7 import run_length_encoding

def compress_file(input_file, output_file):
    list1 = []
    with open(input_file) as inp:
        for character in inp.read():
            list1.append(character)

    compressed = run_length_encoding(list1)
    to_write = []
    for i, j in compressed:
        if i == '\n':
            i = 'new_line'
        txt = i + str(j)
        to_write.append(txt)

    with open(output_file, 'w') as out:
        for i in to_write:
            out.write(i + '\n')

    
    
            
if __name__ == "__main__":
    print(compress_file("test.txt", "comp.txt"))

