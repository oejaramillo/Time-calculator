def add_time(start, duration, day='today'):

    ##Definimos los insumos que vamos a usar

    start_stuff = start.split()
    time = start_stuff[0]
    day_night = start_stuff[1]
    
    time_stuff = time.split(':')
    start_hour = int(time_stuff[0])
    start_minutes = int(time_stuff[1])

    duration_stuff = duration.split(':')
    duration_hour = int(duration_stuff[0])
    duration_minutes = int(duration_stuff[1])

    dic_days = {'Monday':1, 'Tuesday':2, 'Wednesday':3, 'Thursday':4, 'Friday':5, 'Saturday':6, 'Sunday':7}
    days = list(['Monday','Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
    hours = {1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, 11:11, 12:12, 13:1, 14:2, 15:3, 16:4, 17:5, 18:6, 19:7, 20:8, 21:9, 22:10, 23:11, 24:12}

    new_hour = start_hour + duration_hour
    
    new_minutes = start_minutes + duration_minutes
    laps_minutes = int(new_minutes//60)

    new_days = int(new_hour//24)

    new_weeks = int(new_days//7)

    ##Debemos definir cuando reinicia la suma
        #Para los minutos   
    if new_minutes > 59:
        new_minutes = new_minutes-60
        new_hour = new_hour + laps_minutes


        #Para las horas
    if new_hour >= 24:
        new_hour = hours[new_hour-(24*new_days)]
    else:
        if new_hour > 12:
            new_hour = hours[new_hour-12]  

              
    
        #Para los dias
    if day != 'today':
        week_day = dic_days.get(day)
        if new_days >= 1:
            final_day = days[(week_day+new_days-(7*new_weeks))-1]
        else:
            final_day = days[week_day-1]

        
   
        
    
    ##Definimos la salida
        #minutos
    if new_minutes in range(0,10):
        new_minutes = '0{}'.format(new_minutes)

        #el resto 
    if day == 'today':
        if new_days == 1:
            new_time = '{}:{} {} (next day)'.format(str(new_hour), str(new_minutes), new_day_night)
        else:
            if new_days == 0:
                if new_day_night != day_night:
                    new_time = '{}:{} {} (next day)'.format(str(new_hour), str(new_minutes), new_day_night)
                else:
                    new_time = '{}:{} {}'.format(str(new_hour), str(new_minutes), new_day_night)
            else:
                new_time = '{}:{} {} ({} days later)'.format(str(new_hour), str(new_minutes), new_day_night, str(new_days))
            

        
    else:
        if new_days == 1:
            new_time = '{}:{} {}, {} (next day)'.format(str(new_hour), str(new_minutes), day_night, final_day)
        else:
            if new_days == 0:
                new_time = '{}:{} {}, {}'.format(str(new_hour), str(new_minutes), day_night, final_day)
            else:
                new_time = '{}:{} {}, {} ({} days later)'.format(str(new_hour), str(new_minutes), day_night, final_day, str(new_days))
        
        
    

    return print(new_time)

add_time('11:43 PM', '24:20', 'Tuesday')