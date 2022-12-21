'''Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.
https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9/train/python'''


def find_short(s):
    x = s.split()
    max1 = len(x[0])
    for i in x:
        if(len(i) < max1):

            max1 = len(i)
    return max1


print(find_short("Dogecoin Bitcoin LiteCoin Steem Mine Ethereum MadeSafeCoin LiteCoin Dogecoin Steem BTC Monero Ethereum Monero DarkCoin Classic Classic 21inc"))
