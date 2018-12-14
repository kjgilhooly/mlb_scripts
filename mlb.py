import requests
import json

HOST_URL = 'http://lookup-service-prod.mlb.com'

def getTeams():
    req = requests.get("{}/json/named.team_all_season.bam?sport_code='mlb'&all_star_sw='N'&season='2017'".format(HOST_URL))
    if req.status_code == 200:
        data = req.json()
        teams = data['team_all_season']['queryResults'].get('row')
        for team in teams:
            getRoster(team['mlb_org_id'], team['name_display_full'])

def getRoster(code, name):
    print('{} {}'.format(code, name))
    req = requests.get("{}/json/named.roster_40.bam?team_id='{}'".format(HOST_URL, code))
    if req.status_code == 200:
        data = req.json()
        with open('/Users/xriva/Downloads/{}_Roster.json'.format(name), 'w') as teamFile:
            json.dump({'Team': name, 'Roster': data['roster_40']['queryResults'].get('row')}, teamFile)
            teamFile.close()

def main():
    getTeams()

if __name__ == '__main__':
    main()