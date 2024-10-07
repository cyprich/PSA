#!/usr/bin/env python3

if __name__ == "__main__":
	print("hello world")


	def prva_funkcia():
		a = 1 + 4
		return a


	b = prva_funkcia()
	print(b)


	def funkcia_pozdrav(meno):
		return "Ahoj {1} {0} {0} {1}, ako sa mas?".format(meno, "---")


	print(funkcia_pozdrav("jozko"))

	meno = input("Zadajte meno na pozdrav: ")
	print(funkcia_pozdrav(meno))


	class PrvaTrieda:
		def __init__(self):
			self._meno = "peter"
			self._priezvisko = "cyprich"

		def pozdrav(self):
			print(f"ahoj {self._meno} {self._priezvisko}")


	pozdravovac = PrvaTrieda()
	pozdravovac.pozdrav()
