mes = [ 
            "January", 
            "February", 
            "March", 
            "April", 
            "May", 
            "June", 
            "July", 
            "August", 
            "September", 
            "October", 
            "November", 
            "December" 
            ] 

while True: 

    try:
        data = input("Date: ") 

        if "/" in data: 

            m, d, y = data.split("/")

            m = int(m) 
            d = int(d) 
            
        else: 

            partes = data.split(" ") 

            m = mes.index(partes[0]) + 1 
            m = int(m) 

            d = partes[1].replace(",", "") 
            d = int(d) 

            y = partes[2] 

        if m > 12:
            continue

        if d > 31:
            continue 

    
        print(f"{y}-{m:02}-{d:02}")
        break

    except ValueError:
        continue
    except EOFError:
        continue