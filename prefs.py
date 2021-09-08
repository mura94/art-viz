import json

def getLastUsed():
    f = open('prefs.json')
    data = json.load(f)
    f.close()
    return data['lastUsed']

def setLastUsed(settings):
    f = open('prefs.json')
    data = json.load(f)
    f.close()
    data['lastUsed'] = settings
    with open('prefs.json', 'w') as outfile:
        json.dump(data, outfile, sort_keys = True, indent = 4, ensure_ascii = False)

def getProfile(profileName):
    f = open('prefs.json')
    data = json.load(f)
    profiles = data['savedProfiles']
    for p in profiles:
        if(p['name'] == 'Default'):
            return p