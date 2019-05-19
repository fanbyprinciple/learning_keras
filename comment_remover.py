lines = []

print("parsing to lines")
# Parse the file into lines
with open('ashwin.py', 'r') as f:
    print("inside open")
    for line in f:
        print("inside for")
        if line.startswith('#'):
            line = 'new text\n'
            print("inside if")    

        lines.append(line)

print("parsing done!")

# Write them back to the file
with open('ashwin_comment.txt', 'w') as f:
    f.writelines(lines)