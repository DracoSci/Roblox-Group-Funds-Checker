import requests
from threading import Lock, Thread
import concurrent
import itertools
from itertools import cycle
import asyncio, time
import os
import sys
from retrying import retry

global_total = 0
subtotal = 0
"""async def main():
    print(f'{time.ctime()} Hello!')
    await asyncio.sleep(1)
    print(f'{time.ctime()} GOODBYE!')

loop = asyncio.get_event_loop()
task = loop.create_task(main())
loop.run_until_complete(task)
pending = asyncio.all_tasks(loop=loop)
for task in pending:
    task.cancel()
group = asyncio.gather(*pending, return_exceptions=True)
loop.run_until_complete(group)
loop.close()"""


class GroupFunds():
    def __init__(self):
        self.proxycycle = cycle([{'http': f'http://{i.split(":")[2].strip()}:{i.split(":")[3].strip()}@{i.split(":")[0].strip()}:{i.split(":")[1].strip()}'} for i in open("txts/proxies.txt", 'r').readlines()])


        self.roblosecurities = [{'.ROBLOSECURITY' : f'{cookie.strip()}'} for cookie in open("txts/cookies.txt", 'r').readlines()]
        self.groups = [self.grab_groups(security) for security in self.roblosecurities]


        for i in range(len(self.groups)):

            self.balance(self.groups[i])
            globals()['subtotal'] = 0
            print("Cooldown 100 seconds for Proxies")





    def grab_groups(self, cookie):
        """GRAB ID, NAME, AND DISPLAYNAME"""
        r = requests.get("https://users.roblox.com/v1/users/authenticated", cookies=cookie, proxies=next(self.proxycycle)).json()
        print(r)
        id, name = r['id'], r['name']

        """Grabbing the group listings"""
        r = requests.get(f"https://groups.roblox.com/v1/users/{id}/groups/roles", proxies=next(self.proxycycle)).json()

        return [cookie] + [group['group'] for group in r['data']]

    def balance(self, block):
        retry_balance = []

        print(block)
        print("{:^13} | {:^15} | {:^75} | {:^15}".format("GroupID", "Robux", "Exhausted Proxies", "Subtotal"))
        for i in range(1, len(block)):

            try:
                current_proxy = next(self.proxycycle) #This is done to keep track of proxies that are exhausted

                r = requests.get(f"https://economy.roblox.com/v1/groups/{block[i]['id']}/currency", proxies=current_proxy, cookies=block[0]).json()

                globals()['subtotal'] += r['robux']

                print("{:^13} | {:^15} | {:^75} | {:^15}".format(block[i]["id"], r['robux'], '', globals()['subtotal']))
            except:
                #Starting a new place to retry
                retry_balance.append(block[i])
                itertools.chain.from_iterable(retry_balance)

                print("{:^13} | {:^15} | {:^75} | {:^15}".format(block[i]["id"], "0", f"{r['errors'][0]['message']}",  globals()['subtotal']))
        print("{:^13} | {:^15}".format('', globals()['subtotal']))
        #Retrying, after explaining sleep
        print("Finished! However, the block is not finished, retrying after 100 seconds")
        time.sleep(100)

        if len(retry_balance) == 1:
            return subtotal
        else:
            return self.balance([block[0]] + retry_balance)











if __name__ == '__main__':
    x = GroupFunds()


