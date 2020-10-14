import math

def _TriFun(a):
	b =' '.join(a)
	b=b.split(" ", 1)
	pi=math.pi
	if(b[0][0]=='a'):
		n=float(b[1])
		if(b[0]=='asin'):
			out=math.asin(n)*(180/pi)
		elif(b[0]=='acos'):
			out=math.acos(n)*(180/pi)
		elif(b[0]=='atan'):
			out=math.atan(n)*(180/pi)
		sout=str(round(out, 5))+"°"
	elif(b[1][-1]=='°'):
		n=float(b[1][:-1])
		if(b[0]=='sin'):
			out=math.sin(pi/180*n)
		elif(b[0]=='cos'):
			out=math.cos(pi/180*n)
		elif(b[0]=='tan'):
			out=math.tan(pi/180*n)
		sout=str(round(out, 5))
	elif(not b[1][-1]=='°'):
		n=float(b[1][0])
		if(b[0]=='sin'):
			out=math.sin(n)
		elif(b[0]=='cos'):
			out=math.cos(n)
		elif(b[0]=='tan'):
			out=math.tan(n)
		sout=str(round(out, 5))
	return sout