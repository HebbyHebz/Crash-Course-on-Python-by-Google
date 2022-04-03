def seconds(number):
    hours = number // 3600
    minutes = (number - (hours * 3600))//60
    seconds  = number - ((hours * 3600) + (minutes*60))

    return hours, minutes, seconds;


print(seconds(10800))

h, m, s = seconds(7000)
print(h,m,s)