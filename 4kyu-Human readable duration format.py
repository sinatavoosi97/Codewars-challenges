
# Description:
# Your task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds, in a human-friendly way.

# The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.

# It is much easier to understand with an example:

# * For seconds = 62, your function should return 
#     "1 minute and 2 seconds"
# * For seconds = 3662, your function should return
#     "1 hour, 1 minute and 2 seconds"
# For the purpose of this Kata, a year is 365 days and a day is 24 hours.

# Note that spaces are important.

# Detailed rules
# The resulting expression is made of components like 4 seconds, 1 year, etc. In general, a positive integer and one of the valid units of time, separated by a space. The unit of time is used in plural if the integer is greater than 1.

# The components are separated by a comma and a space (", "). Except the last component, which is separated by " and ", just like it would be written in English.

# A more significant units of time will occur before than a least significant one. Therefore, 1 second and 1 year is not correct, but 1 year and 1 second is.

# Different components have different unit of times. So there is not repeated units like in 5 seconds and 1 second.

# A component will not appear at all if its value happens to be zero. Hence, 1 minute and 0 seconds is not valid, but it should be just 1 minute.

# A unit of time must be used "as much as possible". It means that the function should not return 61 seconds, but 1 minute and 1 second instead. Formally, the duration specified by of a component must not be greater than any valid more significant unit of time.

# Strings Date Time Algorithms



def format_duration(seconds):


    list_se=[]


    year=seconds//(365*24*3600)


    day=(seconds-(year*(365*24*3600)))//(24*3600)


    hour=(seconds-(((year*(365*24*3600))+(day*(24*3600)))))//(3600)


    minutes=(seconds-((year*(365*24*3600))+(day*(24*3600))+(hour*3600)))//60

    if year==0 and day==0 and hour==0 and minutes==0:

        second=seconds

    else:
        second=(seconds-((year*(365*24*3600))+(day*(24*3600))+(hour*3600)+( minutes*60)))

    #==================================================================================================================================

    list_se.append("A") if year==0 else list_se.append(year)
    
    list_se.append("A") if year==0 else list_se.append("year") if year==1 else list_se.append("years")

    list_se.append("A") if year==0 else list_se.append(", ")

    

    list_se.append("A") if day==0 else list_se.append(day)

    list_se.append("A") if day==0 else list_se.append("day") if day==1 else list_se.append("days")

    list_se.append("A") if day==0 else list_se.append(", ")

    

    list_se.append("A") if hour==0 else list_se.append(hour)
    
    list_se.append("A") if hour==0 else list_se.append("hour") if hour==1 else list_se.append("hours")

    list_se.append("A") if hour==0 else list_se.append(", ")

   

    list_se.append("A") if minutes==0 else list_se.append(minutes)
    
    list_se.append("A") if minutes==0 else list_se.append("minute") if minutes==1 else list_se.append("minutes")

    if second !=0:

        list_se.append("A") if minutes==0 else list_se.append(" and ")



    list_se.append("A") if second==0 else list_se.append(second)


    j=0
    if second==1 :
          
          list_se.append("second")

    elif second>1 :

        list_se.append("seconds")

    elif seconds==0:
            list_se.append("now")

    else:
        j+=1



    message=[]
    i=0
    for item in list_se:


        if item == "A":
            i+=1
        else:
            message.append(item)


    if len(message)==3:

        message.pop(-1)


    if len(message)  < 12 :

        if len(message) > 6 :

               message[-3]=" and "


    message_01=""
    for text in message :

        if type(text)==int: 

            message_01+=str(text)
            message_01+=" "
        else:

            message_01+=text



    return  message_01



print(format_duration(2854668))








