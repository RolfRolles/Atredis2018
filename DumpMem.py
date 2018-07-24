import telnetlib

def ReadByte(t,addr):
	if addr & 0xF == 0:
		print "Fetching byte from %04x" % addr
	t.write("read %4x\n" % addr)
	str = t.read_until("arkos>")
	#print str
	return int(str.split("\n")[0].split("= $")[1],16)
	
def ReadRange(t,addr,len):
	return map(lambda i: ReadByte(t,addr+i),xrange(len))

ranges = [
(0x0, 0x100),
(0x100,0x100),
(0x200,0x2000-0x200),
(0x4000,0xF000-0x4000),
(0xF001,0xEFF),
(0xFF00,0x100)
]
	
t = telnetlib.Telnet("arkos.atredis.com",4444)
str = t.read_until("arkos>")

for (begin,len) in ranges:
	data = ReadRange(t,begin,len)
	newFile = open("data-%04x-%04x.bin" % (begin,begin+len-1), "wb")
	ba = bytearray(data)
	newFile.write(ba)
	newFile.close()
		