def add_time(start, duration):

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

    days = {1:'Monday', 2:'Tuesday', 3:'Wednesday', 4:'Thursday', 5:'Friday', 6:'Saturday', 7:'Sunday'}
    hours = {1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, 11:11, 12:12, 13:1, 14:2, 15:3, 16:4, 17:5, 18:6, 19:7, 20:8, 21:9, 22:10, 23:11, 24:12}
    minutes = list(range(1,61))

    new_hour = start_hour + duration_hour
    new_minutes = start_minutes + duration_minutes
    new_days = int(new_hour/24)

    ##Debemos definir cuando reinicia la suma
        #Para las horas
    if new_hour > 12:
        if new_hour > 24:
            new_hour = hours[new_hour-(24*new_days)]
        else:
            new_hour = hours[new_hour-12]        
    
        #Para el periodo %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Revisar %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    if new_days/12 % 2 == 1:
        if day_night == 'PM':
            day_night = 'AM'
        else:
            day_night = 'PM'
        
        

    
    
        
        #Para los minutos         

    if new_minutes > 60:
        laps_minutes = int(new_minutes/60)
        new_minutes = new_minutes-60
        new_hour = new_hour + laps_minutes

    ##Definimos la salida

    

    if new_minutes in range(0,10):
        new_minutes = '0{}'.format(new_minutes)

    
    new_time = '{}:{} {}'.format(str(new_hour   ), str(new_minutes), day_night)

    return print()

add_time('6:30 PM', '205:12')