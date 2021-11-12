version = input().split('.')
version_int = [int(x) for x in version]

if version_int[2] +1 <= 9:
    version_int[2] += 1
elif version_int[2] + 1 > 9 and version_int[1] + 1 <= 9:
    version_int[2] = 0
    version_int[1] += 1
elif version_int[2] + 1 > 9 and version_int[1] + 1 > 9 and version_int[0] + 1 <= 9:
    version_int[2] = 0
    version_int[1] = 0
    version_int[0] += 1

version_str = [str(x) for x in version_int]
print('.'.join(version_str))
