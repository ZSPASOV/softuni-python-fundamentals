def receive_grade(value):
# ako ne go dadem None v tozi sluchai s edin return nakraq i dadem stoinost izvun range [2:6] shte dade error
    result = None
    if 2.00 <= value < 3.00:
        result = 'Fail'
    if 3.00 <= value < 3.50:
        result = 'Poor'
    if 3.50 <= value < 4.50:
        result = 'Good'
    if 4.50 <= value < 5.50:
        result = 'Very Good'
    if 5.50 <= value <= 6.00:
        result = 'Excellent'
    return result

value = float(input())
print(receive_grade(value))