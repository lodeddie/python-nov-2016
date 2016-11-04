
def draw_stars(arr):
	for num in arr:
		if type(num)==int:
			print "*" * num
		else:
			print num[0] * len(num)
draw_stars(["tom","dan",1,3,5,7,25])
