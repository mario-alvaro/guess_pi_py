#aproximación a pi prueba
#rectángulo (lado 2r) y circunferencia de radio r
#área rectángulo=4*r^2
#área circunf=pi*r^2
#píxeles dentro/pixeles total = pi/4
#píxeles dentro/pixeles total*4 = pi
# pi ~= 3,1415926535897932384626433832795028841971693993751058209

import math
r = int(input("Radio de la circunferencia: "))
r2 = 2*r#lados del rectangulo
pixelesTotal = 0
pixelesDentro = 0
pi = 0;
pixelesTotal = r2*r2
for i in range(r2):#de 0 a r2-1
    for j in range(r2):#(r,r) es el centro aproximado
        distCol = j-r
        distFil = i-r
        dist = math.sqrt(distCol**2+distFil**2)
        if dist <= r :
            pixelesDentro = pixelesDentro+1
			
	#show progress
    if i/(r2)*100%5 < 0.01:#con numeros primos no se puede conseguir resto == 0
        print(str(int(i/(r2)*100)) +"%")#se muestra algo para ver el progreso
    

pi = pixelesDentro/pixelesTotal*4
print("Pi calculado: "+str(pi))
            
        
        
