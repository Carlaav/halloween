def hanoi_carla(mover_desde, apoyo, mover_a, n):
	if n > 0:

		hanoi_carla(mover_desde, mover_a, apoyo, n-1)

		print("Mover un disco de oro de la agua {} -> {} usando {}."
		.format(mover_desde, mover_a, apoyo))

		hanoi_carla(apoyo, mover_desde, mover_a, n-1)

if __name__ == "__main__":
	hanoi_carla(1, 2, 3, 5)



