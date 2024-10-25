# wap to copy the contents of one file into another. input both file names with path from user

def copy_file_contents(source_file, destination_file):
    with open(source_file, 'r') as src:
        content = src.read()

    with open(destination_file, 'w') as dest:
        dest.write(content)

    print(f'Contents copied from {source_file} to {destination_file} successfully.')

source_file = input('Enter the source file name with path: ')
destination_file = input('Enter the destination file name with path: ')

copy_file_contents(source_file,destination_file)

