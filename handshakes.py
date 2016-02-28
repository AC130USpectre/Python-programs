import vk
import time
import pickle
import sys

with open('access_token.txt', 'r') as file:
    api = vk.API(vk.Session(access_token = file.readline()), v = '5.45', lang = 'ru') # for you
#api = vk.API(vk.Session(), v = '5.45', lang = 'ru') # for any user

errorLogs = open('{}_error.log'.format(sys.argv[1]), 'w') # redirect exceptions messages to log file

waves = [{int(sys.argv[1])}] # wave zero - root user
while True: # until user do not interrupt
    while True: # request for interruption
        ask = input('Get next wave? [Y/N]\n')
        if ask == 'Y':
            break
        elif ask == 'N':
            print('Exit!')
            sys.exit(0)
        else:
            continue
    wave = set()
    last_wave = list(waves[-1])
    k = 0
    users = []
    for i in range(len(last_wave)): # for each user in last wave...
        print('{}/{}'.format(str(i + 1), str(len(last_wave)))) # count our current position in last wave
        users.append(str(last_wave[i])) # buffer for api method
        k += 1 # count until 25 users...
        if k == 25:
            while True: # trying to get 25 list of friends for 25 users (why 25? API restrictions : https://vk.com/dev/execute)
                try:
                    friends = api.execute.getFriendsOf(user1 = users[0], user2 = users[1], user3 = users[2], user4 = users[3], user5 = users[4], user6 = users[5], user7 = users[6], user8 = users[7], user9 = users[8], user10 = users[9], user11 = users[10], user12 = users[11], user13 = users[12], user14 = users[13], user15 = users[14], user16 = users[15], user17 = users[16], user18 = users[17], user19 = users[18], user20 = users[19], user21 = users[20], user22 = users[21], user23 = users[22], user24 = users[23], user25 = users[24])
                    break
                except Exception as e:
                    print('Exception!')
                    print(e, file = errorLogs)
                    time.sleep(3) # wait for the next request
            for j in friends: # got 25 lists and for each list
                if j: # if isn't None (which means that user deactivated and we don't have access to the friends list)
                    wave.update(set(j))
            k = 0 # next 25 users...
            users = []
    if k > 0: # if full number of users is not divisible by 25
        for i in users: # for each rest...
            while True:
                try:
                    friends = api.friends.get(user_id = int(i))['items'] # get friends list
                    break
                except Exception as e:
                    print('Exception!')
                    print(e, file = errorLogs)
                    if str(e).find('user deactivated') != -1: # no access to friends list
                        friends = []
                        break
                    time.sleep(3) # wait for the next request
            wave.update(set(friends))
    for j in waves: # no repeats
        wave -= j
    print('Got {} new elements'.format(len(wave)))
    waves.append(wave.copy())
    print('Write data...')
    with open('{}_waves.bin'.format(sys.argv[1]), 'wb') as file: # flush data
        pickle.dump(waves, file)
