
class Data: 
	def __init__(self, x, y): 
		self.x = x 
		self.y = y 

def interpolate(f: list, xi: int, n: int) -> float: 

	result = 0.0
	for i in range(n): 
 
		term = f[i].y 
		for j in range(n): 
			if j != i: 
				term = term * (xi - f[j].x) / (f[i].x - f[j].x) 

		result += term 

	return result 

if __name__ == "__main__": 

	f = [Data(0, 0), Data(1, 1), Data(3, 81), Data(4, 256), Data(5, 625)] 

	print("Value of f(2) is :", interpolate(f, 2, 5)) 
