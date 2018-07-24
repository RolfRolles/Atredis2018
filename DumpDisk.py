import telnetlib

t = telnetlib.Telnet("arkos.atredis.com",4444)
str = t.read_until("arkos>")

for i in xrange(1,0x40):
	t.write("write 0130 00\n")
	str = t.read_until("arkos>")
	t.write("write 0131 00\n")
	str = t.read_until("arkos>")
	t.write("write 0132 %02d\n" % i)
	str = t.read_until("arkos>")
	t.write("write 0133 00\n")
	str = t.read_until("arkos>")
	t.write("call 822c\n")
	str = t.read_until("arkos>")
	newFile = open("file-0000-%04x.bin" % i, "wb")
	ba = bytearray(str)
	newFile.write(ba)
	newFile.close()
	print str

	
