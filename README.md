# Github Username Searcher

> Inspired by various other projects like this one.

This script batches requests to the Github website to find usernames that return a 200 status code, which means that profile is registered, or a 404 status code, which means that username is not registered or the username has been banned.

I've also included a feature which includes a common username list to search for human readable names, beyond just n-letter availabile usernames.

### Why are the names I get back not working?

The majority of rare unclaimed names you'll find are likely banned/restricted by Github, since we can't tell if the username is unclaimed/restricted when we query the profile page. Don't worry, if you have a username you really want just shoot Github an email and they'll often release it for you.

### I'm getting rate limited!

This script has a reputation for shutting down your building's Github connection for 15 minutes (don't run this at a co-working space accidentally, like me). If you want to run this for longer you'll need to setup some proxy or VPN scheme to get around the rate limiting.

### Where can I find different wordlists?

There's a lot of great username wordlist from security research repositories. I've included one which has around ~80,000 names but you can find lists in the 10s/100 millions of names out there. Start here (not that you'll be querying Github 100 million times): https://github.com/danielmiessler/SecLists/tree/master/Usernames
