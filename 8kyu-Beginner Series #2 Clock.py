

def past(h, m, s):

    seconds=0

    if 0 <= h <= 23 and 0 <= m <= 59 and 0 <= s <= 59:

        seconds+=(h*3600)

        seconds+=(m*60)

        seconds+=(s)

    else:

        return "Error"

    return seconds*1000

        

print(past(0,1,1))