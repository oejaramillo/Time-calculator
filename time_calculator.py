def add_time(start, duration):

    ##Defirnimos los insumos que vamos a usar

    start_stuff = start.split()
    time = start_stuff[0]
    day_night = start_stuff[1]
    
    time_stuff = time.split(':')
    start_hour = int(time_stuff[0])
    start_minutes = int(time_stuff[1])

    duration_stuff = duration.split(':')
    duration_hour = int(duration_stuff[0])
    duration_minutes = int(duration_stuff[1])

    days = list(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
    hours = list(range(1,13))
    minutes = list(range(1,61))

    new_hour = start_hour + duration_hour
    new_minutes = start_minutes + duration_minutes

    ##Debemos definir cuando reinicia la suma
        #Para las horas

    if new_hour >= 12:
        laps_hours = int(duration_hour/12)
        new_hour = duration_hour-12*laps_hours
        if laps_hours % 2 == 1:
            if day_night == 'PM':
                day_night = 'AM'
            else:
                day_night = 'AM'
        
        #Para los minutos         

    if new_minutes > 60:
        laps_minutes = int(new_minutes/60)
        new_minutes = new_minutes-60
        new_hour = new_hour + laps_minutes

    ##Definimos la salida

    if new_hour == 0:
        new_hour = '12'

    if new_minutes in range(0,10):
        new_minutes = '0{}'.format(new_minutes)

    
    new_time = '{}:{} {}'.format(str(new_hour   ), str(new_minutes), day_night)

    return print(new_time)

add_time('12:05 PM', '2:02')