def add_time(start, duration, day='today'):

    ##Definimos los insumos que vamos a usar
    start_hours, start_minutes = start.split(':') 
    start_hours = int(start_hours)
    start_minutes = int(start_minutes.split()[0])

    day_night = start.split()[1]

    #para la duracion
    duration_hours, duration_minutes = duration.split(':')
    duration_hours = int(duration_hours)
    duration_minutes = int(duration_minutes)
    
    if (start_hours + duration_hours) < 12:
        day_night = start.split()[1]
    else:  
        if day_night == 'PM':
            start_hours += 12

    #un diccionario para los dias
    dic_days = {'Monday':1, 'Tuesday':2, 'Wednesday':3, 'Thursday':4, 'Friday':5, 'Saturday':6, 'Sunday':7}

    #sumamos
    new_hours = (start_hours + duration_hours) % 24
    new_minutes = (start_minutes + duration_minutes) % 60

    if (start_minutes + duration_minutes) >= 60:
        new_hours = new_hours + 1
    
    #definimos el formato de 12 horas
    if new_hours >= 12:
        new_hours -= 12
        day_night = 'PM'
    else:
        day_night = 'AM'

    #contamos los dias y las semanas
    new_days = int(round((new_hours + duration_hours)/24, 0))
    

    #contamos los dias
    if day != 'today':
        week_day = dic_days.get(day)
        new_week_day = (week_day + new_days) % 7
        final_day = list(dic_days.keys())[list(dic_days.values()).index(new_week_day)]
    
    #definimos la salida
    if new_hours == 0:
        new_hours = 12

    if (start_hours + duration_hours) % 2 == 1:
        if day_night == 'PM':
            day_night = 'AM'
        else:
            day_night = 'PM'

    if duration_hours == 0:
        if duration_minutes == 0:
            day_night = start.split()[1]
        else:
            if (start_minutes + duration_minutes) >= 60:
                if day_night == 'PM':
                    day_night = 'AM'
                else:
                    day_night = 'PM'
    
    #Definimos formatos  
    new_time = f"{new_hours}:{new_minutes:02d} {day_night}"
    
    if day == 'today':
        if new_days == 0:
            if start.split()[1] == 'PM':
                if start.split()[1] != day_night:
                    new_time = f"{new_time} (next day)"
                else:
                    new_time = f"{new_time}"
        else:
            if new_days == 1:
                new_time = f"{new_time} (next day)"
            else:
                if new_days > 1:
                    new_time = f"{new_time} ({new_days} days later)"
                else:
                    if start.split()[1] == 'PM':
                        if start.split()[1] != day_night:
                            new_time = f"{new_time} (next day)"
    else:
        if new_days == 0:
            if start.split()[1] == 'PM':
                if start.split()[1] != day_night:
                    new_time = f"{new_time}, {final_day} (next day)"
                else:
                    new_time = f"{new_time}, {final_day}"
        else:
            if new_days == 1:
                new_time = f"{new_time}, {final_day} (next day)"
            else:        
                if new_days > 1:
                    new_time = f"{new_time}, {final_day} ({new_days} days later)"
                else:
                    if start.split()[1] == 'PM':
                        if start.split()[1] != day_night:
                            new_time = f"{new_time}, {final_day} (next day)"
                        else:
                            new_time = f"{new_time}, {final_day}"
                    else:
                        new_time = f"{new_time}, {final_day}"


    return print(new_time)

add_time("2:59 AM", "24:00", "Wednesday")