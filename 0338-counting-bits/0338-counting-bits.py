class Solution:
	def countBits(self, n: int) -> List[int]:
		result = []
		for i in range(n + 1):
			str_hex = str(bin(i)[2:])
			result.append(str_hex.count("1"))

		return result