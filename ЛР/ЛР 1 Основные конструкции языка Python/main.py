import math
import sys

def calculate(A, B, C):
	D = B * B - 4 * A * C
	print(f"D = {D}")
	if D > 0:
		t = (-B - math.sqrt(D)) / (2 * A)
		print(t)
		if t > 0:
			x1 = math.sqrt((-B - math.sqrt(D)) / (2 * A))
			x2 = -x1

			print(f"x₁ = {x1}")
			print(f"x₂ = {x2}")

		t = (-B + math.sqrt(D)) / (2 * A)
		print(t)
		if t > 0:
			x1 = math.sqrt((-B + math.sqrt(D)) / (2 * A))
			x2 = -x1

			print(f"x₁ = {x1}")
			print(f"x₂ = {x2}")
		else:
			print("Действительных корней нет")
	elif D == 0:
		t = -B / (2 * A)
		if t > 0:
			x1 = math.sqrt(t)
			x2 = -x1
			print(f"x₁ = {x1}")
			print(f"x₂ = {x2}")
		else:
			print("Действительных корней нет")	
	else:
		print("Корней нет")

def main():
	A = 1
	B = 1
	C = 1
	try:
		A = float(sys.argv[1])
		B = float(sys.argv[2])
		C = float(sys.argv[3])
		print (sys.argv)
	except Exception as e:
		print("Коэффициенты некорректные")

		A = float(input("Введите коэффициент A\n> "))
		if A == 0:
			print("Коэффициент А должен быть не равен 0")
			exit()

		B = float(input("Введите коэффициент B\n> "))
		C = float(input("Введите коэффициент C\n> "))

				
	calculate(A, B, C)

# 1 -10 9
# 1 -5 -3660
# 60 -20 -5
		
if __name__ == "__main__":
	main()