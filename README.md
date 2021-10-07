# d2i

## <hr> A minimalist extension of the statistics module for operations on discrete series. `Only a function` <hr>

### Code
```py
class D2I(Exception): pass

def d2i(*, x: list, f: list) -> list:
	"""
	Convert discrete series into
	individual and return it for operations
	"""
	if len(x) == len(y): return [float(k) for k, v in dict(zip(x, f)).items() for n in range(int(v))]
	else: raise D2I("Unequal freq-obsn count")
```

### This could be shortened by `lambda`:
```py
d2i = lambda x, f: [float(k) for k, v in dict(zip(x, f)).items() for n in range(int(v))]
```

### <hr> Usage
```py
import statistics
import d2i


marks 	 = [15, 20, 22, 23, 27, 35, 18]
students = [ 8,  4,  7,  3,  8,  7,  5]

chunk 	 = d2i.d2i(x=marks, f=students)

# Lambda implementation
# d2i 	= lambda x, f: [float(k) for k, v in dict(zip(x, f)).items() for n in range(int(v))]
# chunk = d2i(marks, students) # Be careful about argument positioning

print(f"Average = {statistics.mean(chunk)}")
print(f"Median  = {statistics.median(chunk)}")
print(f"Mode    = {statistics.mode(chunk)}")
```
