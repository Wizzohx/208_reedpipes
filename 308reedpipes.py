#!/usr/bin/env python3

from sys import argv, stderr, exit
from math import factorial

class BadArgumentError(Exception):
	def __init__(self, message, errors = "BadArgumentError"):
		super().__init__(message)
		self.errors = errors

class calcul():
	result = []
	ord = []
	abs = [0, 5, 10, 15, 20]
	vec = [0, None, None, None, 0]
	var = {'r0': 0, 'r5': 0, 'r10': 0, 'r15': 0, 'r20': 0, 'n': 0}	
	def __init__(self, argument, total=0):
		for arg, i in zip(self.var, range(1, len(argument))):
			if float(argument[i]) <= 0:
				raise BadArgumentError("'{}' must be positive (is {})".format(arg, argument[i]))
			self.var[arg] = float(argument[i])
			if self.var[arg] is not self.var['n']:
				self.ord.append(self.var[arg])

	def display(self):
		print("vector result: [{:.1f}, {:.1f}, {:.1f}, {:.1f}, {:.1f}]".format(self.vec[0] if round(self.vec[0], 1) != 0 else 0, self.vec[1] if round(self.vec[1], 1) != 0 else 0, self.vec[2] if round(self.vec[2], 1) != 0 else 0, self.vec[3] if round(self.vec[3], 1) != 0 else 0, self.vec[4] if round(self.vec[4], 1) != 0 else 0))
		for i in range(int(self.var['n'])):
			print("abscissa: {:.1f} cm\tradius: {:.1f} cm".format(20 / (self.var['n'] - 1) * i, self.result[i]))

	def algo(self):
		a = 6 * (self.var['r10'] - 2 * self.var['r5'] + self.var['r0']) / 50
		b = 6 * (self.var['r15'] - 2 * self.var['r10'] + self.var['r5']) / 50
		c = 6 * (self.var['r20'] - 2 * self.var['r15'] + self.var['r10']) / 50
		self.vec[2] = (b - (a + c) / 4) * 4 / 7
		self.vec[1] = a / 2 - 0.25 * self.vec[2]
		self.vec[3] = c / 2 - 0.25 * self.vec[2]
		for d in range(int(self.var['n'])):
			x = 20 / (self.var['n'] - 1) * d
			i = int((x - 0.01) / 5) + 1
			result = (- self.vec[i - 1] / 30 * pow(x - self.abs[i], 3) + self.vec[i] / 30 * pow(x - self.abs[i - 1], 3) - (self.ord[i - 1] / 5 - 5 / 6 * self.vec[i - 1]) * (x - self.abs[i]) + (self.ord[i] / 5 - 5 / 6 * self.vec[i]) * (x - self.abs[i - 1]))
			self.result.append(result)

def main():
	if len(argv) != 7:
		raise BadArgumentError("Usage: ./308reedpipes r0 r5 r10 r15 r20 n")
	obj = calcul(argv)
	obj.algo()
	obj.display()

if __name__ == "__main__":
	try:
		main()
	except BaseException as error:
		stderr.write(str(type(error).__name__) + ": {}\n".format(error))
		exit(84)