x = int(input("Número: "))
y = int(input("Número: "))
z= int(input("Número: "))

def max (x, y, z):
	if x > y and x > z:
		print ("O maior número é: ", x)

	elif y > x and y > z:
		print ("O maior número é: ", y)

	else:
		print ("O maior número é: ", z)
		
max (x,y,z)
