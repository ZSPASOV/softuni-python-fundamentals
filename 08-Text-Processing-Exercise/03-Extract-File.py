link = input().split('\\') # you need a second \ in the split because first is for escaping quotes
#link = input().split('\ '.strip()) - same as line above
file_and_extension = link[-1]
file_and_extension_split = file_and_extension.split('.')
file = file_and_extension_split[0]
extension = file_and_extension_split[1]
print(f'File name: {file}')
print(f'File extension: {extension}')