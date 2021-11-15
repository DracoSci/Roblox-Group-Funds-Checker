# Roblox-Ground-Funds-Checker
Very simple program with two very simple files.
# Proxies.txt
It is recommended that one use proxies, formatted in the file as " IP:PORT:USERNAME:PASSWORD"
I highly recommend using webshare.io, as they give you 10 free proxies to start with and it is already formatted properly
# Cookies.txt
Simple as it gets, just place your .ROBLOSECURITY's in, one for each line, and your good!

# Whats Returned?
(Exhausted Proxies refers to proxies that have sent too many requests to the Roblox API and receive "TOO MANY REQUESTS" as a response instead of the usual output)
For each roblosecurity, the group id, current robux within said group id, possible errors, and a subtotal on the side. The groups that were missed due to Exhausted Proxies are sent into the same method once again after 100 seconds. An issue to be noted is that errors that are not due to Exhausted Proxies, e.g. Payout-Restricted, Deleted Groups, Not-Owner, may be caught in an infinite loop. (Will fix at a later date)

