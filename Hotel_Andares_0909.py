#Retorna andares do Hotel.1109
andar_hotel = 0
for i in range(20 ):
  andar_hotel = andar_hotel + 1
  if (andar_hotel == 13):
    continue
  if (andar_hotel == 21):
    break
  print("O número do andar é:", andar_hotel)
  
  -------------------------------------------------
#Retorna andares do Hotel em ordem decrescente (20, 19, 18 ...):
andar_hotel = 21
while andar_hotel != 1:  
    andar_hotel = andar_hotel -1
    if (andar_hotel == 13):
      continue
    if (andar_hotel == 0):
      break 
    print("O número do andar é:", andar_hotel) 
    ---------------------------------------------------------------------------------