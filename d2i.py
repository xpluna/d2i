class D2I(Exception): pass

def d2i(*, x: list, f: list) -> list:
	"""
	Convert discrete series into
	individual and return it for operations
	"""
	if len(x) == len(y): return [float(k) for k, v in dict(zip(x, f)).items() for n in range(int(v))]
	else: raise D2I("Unequal freq-obsn count")
