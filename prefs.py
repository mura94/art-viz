import json

def getLastUsed():
    f = open('prefs.json')
    data = json.load(f)
    print(data['lastUsed'])
    f.close()
    return data['lastUsed']

def setLastUsed(settings):
    print('settings:')
    print(settings)
    f = open('prefs.json')
    data = json.load(f)
    f.close()
    data['lastUsed'] = settings
    print('data:')
    print(data)
    with open('prefs.json', 'w') as outfile:
        json.dump(data, outfile, sort_keys = True, indent = 4, ensure_ascii = False)

def getProfile(profileName):
    f = open('prefs.json')
    data = json.load(f)
    profiles = data['savedProfiles']
    for p in profiles:
        # print(p)
        if(p['name'] == 'Default'):
            return p

# lastUsed = getLastUsed()
# lastUsed['width'] = str(500)
# print('lastUsed:')
# print(lastUsed)
# setLastUsed(lastUsed)

# {
#     "lastUsed":{
#         "image": "garlic.png",
#         "width": "24",
#         "height": "18",
#         "depth": ".5",
#         "renderer": "CYCLES",
#         "frameType": "BlackFloatingFrame",
#         "wallColor": "E4DED5"
#     },
#     "savedProfiles":
#     [
#         {
#             "name": "Default",
#             "image": "garlic.png",
#             "width": "24",
#             "height": "18",
#             "depth": ".5",
#             "renderer": "CYCLES",
#             "frameType": "BlackFloatingFrame",
#             "wallColor": "E4DED5"
#         }
#     ]
# }