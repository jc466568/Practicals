
COLOUR_NAME = {'AliceBlue': '#fof8ff', 'aquamarine4': '#458b74', 'azure4': '#838b8b', 'bisque3': '#cdb79e',
               'blue4': '#00008b', 'brown2': '#ee3b3', 'burlywood1': '#ffd39b', 'CadetBlue3': '#7ac5cd',
               'chartreuse4': '#458b00', 'coral': '#ff7f50'}
# finished = False
# try:
#     while not finished:
#         name = input("Enter colour name: ")
#         if name in COLOUR_NAME.keys():
#             print(COLOUR_NAME[name])
#         if name == "":
#             print("Done")
#             finished = True
#             print("Invalid")
# except ValueError:
#     print("Invalid")


name = input("Enter colour name: ")
while name != "":
    if name in COLOUR_NAME:
        print(COLOUR_NAME[name])
    else:
        print("Invalid")
    name = input("Enter colour name: ")
