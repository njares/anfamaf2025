from colorama import Fore, Style
import struct

def print_float(x):
	bits = bin(struct.unpack('!Q',struct.pack('!d',x))[0])[2:].zfill(64)
	#bits_color = Fore.CYAN + bits[0] +'\t' + Fore.GREEN + bits[1:12] +'\t'+ Fore.RED + bits[12:] + Style.RESET_ALL
	bits_color = Fore.CYAN + bits[0] +'\t' + Fore.GREEN + bits[1:12] +'\t'+ Fore.WHITE + bits[12:] + Style.RESET_ALL
	decimal = ''
	if bits[0] == '0':
		decimal += Fore.CYAN + '+1' + '\t'
	else:
		decimal += Fore.CYAN + '-1' + '\t'
	decimal_mantisa = 0.
	bits_mantisa = list(bits[12:])
	decimal_add = 1/2
	while bits_mantisa:
		current_bit = int(bits_mantisa.pop(0))
		if current_bit:
			decimal_mantisa += decimal_add
		decimal_add /= 2
	if int(bits[1:12],2) == 0:
		if decimal_mantisa == 0.:
			decimal += Fore.GREEN + str(int(bits[1:12],2) - 1023) + '\t\t'
		else:
			decimal += Fore.GREEN + str(int(bits[1:12],2) - 1023 + 1) + '\t\t'
	else:
		decimal_mantisa += 1
		decimal += Fore.GREEN + str(int(bits[1:12],2) - 1023) + '\t\t'
	#decimal += Fore.RED + str(decimal_mantisa) + Style.RESET_ALL
	decimal += Fore.WHITE + str(decimal_mantisa) + Style.RESET_ALL
	print(bits_color)
	print(decimal)
