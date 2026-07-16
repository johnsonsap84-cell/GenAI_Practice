def make_multiplier(factor):
	"""Return a function that multiplies its numeric arguments by factor.

	The returned function accepts any number of positional args and keyword
	args; it multiplies all numeric values and preserves other values.
	"""
	def multiplier(*args, **kwargs):
		# process positional arguments
		new_args = [a * factor if isinstance(a, (int, float)) else a for a in args]
		# process keyword arguments
		new_kwargs = {k: (v * factor if isinstance(v, (int, float)) else v)
					  for k, v in kwargs.items()}
		return new_args, new_kwargs

	return multiplier


if __name__ == '__main__':
	doubler = make_multiplier(2)
	tripler = make_multiplier(3)

	# positional args only
	print(doubler(1, 2, 3))            # ([2, 4, 6], {})

	# kwargs only
	print(tripler(a=4, b=5))           # ([], {'a': 12, 'b': 15})

	# mixed args and kwargs, non-numeric preserved
	print(doubler(10, 'x', y=3, z='hi'))
	# expected: ([20, 'x'], {'y': 6, 'z': 'hi'})
