from PIL import Image

def colorAvg(a,b):
  ar, ag, ab, ax= a
  br, bg, bb, bx = b
  r = round((ar+br)/2)
  g = round((ag+bg)/2)
  b = round((ab+bb)/2)
  string=str(r)
  string+=', '
  string+=str(g)
  string+=', '
  string+=str(b)
  string+=', 255'
  return eval(string)

colors = []
colorInput = " "
while colorInput != "":
  colorInput = input("Color: ")
  if colorInput != "":
    colors.append(colorInput)

for i in range(len(colors)):
  color=colors[i]

  powdername='blocks\plastic_'
  powdername+=color
  powdername+='_cut.png'

  plasticname='items\plastic_'
  plasticname+=color
  plasticname+='.png'

  concreteIm = Image.open(powdername, 'r')
  concrete = concreteIm.load()

  a = concrete[0,15]
  e = concrete[0,0]

  c = colorAvg(a,e)
  b = colorAvg(a,c)
  d = colorAvg(c,e)

  plasticIm = Image.new('RGBA', (16, 16), (0, 0, 0, 0))
  plastic = plasticIm.load()

  plastic[9,13] = a
  plastic[8,13] = a
  plastic[7,13] = a
  plastic[6,13] = a
  plastic[5,12] = a
  plastic[4,12] = a
  plastic[3,11] = a
  plastic[3,10] = a
  plastic[10,12] = a
  plastic[11,12] = a
  plastic[12,11] = a
  plastic[12,10] = a
  plastic[13,9] = a
  plastic[13,8] = a
  plastic[13,7] = a
  plastic[13,6] = a
  plastic[12,5] = a
  plastic[12,4] = a
  plastic[11,3] = a
  plastic[10,3] = a
  plastic[9,2] = a
  plastic[8,2] = a

  plastic[9,12] = b
  plastic[11,11] = b
  plastic[12,9] = b
  plastic[11,4] = b
  plastic[4,11] = b
  plastic[2,9] = b
  plastic[2,8] = b
  plastic[2,7] = b
  plastic[2,6] = b
  plastic[3,5] = b
  plastic[3,4] = b
  plastic[4,3] = b
  plastic[5,3] = b
  plastic[6,2] = b
  plastic[7,2] = b

  plastic[6,12] = c
  plastic[7,12] = c
  plastic[8,12] = c
  plastic[8,11] = c
  plastic[9,11] = c
  plastic[10,11] = c
  plastic[10,10] = c
  plastic[11,10] = c
  plastic[11,9] = c
  plastic[11,8] = c
  plastic[12,8] = c
  plastic[12,7] = c
  plastic[12,6] = c

  plastic[3,9] = d
  plastic[4,10] = d
  plastic[5,11] = d
  plastic[6,11] = d
  plastic[7,11] = d
  plastic[8,10] = d
  plastic[9,10] = d
  plastic[10,9] = d
  plastic[10,8] = d
  plastic[11,7] = d
  plastic[11,6] = d
  plastic[11,5] = d
  plastic[10,4] = d
  plastic[9,3] = d

  plastic[10,5] = e
  plastic[10,6] = e
  plastic[10,7] = e
  plastic[9,7] = e
  plastic[9,8] = e
  plastic[9,9] = e
  plastic[8,8] = e
  plastic[8,9] = e
  plastic[7,9] = e
  plastic[6,9] = e
  plastic[5,9] = e
  plastic[4,9] = e
  plastic[4,8] = e
  plastic[3,8] = e
  plastic[3,7] = e
  plastic[3,6] = e
  plastic[7,10] = e
  plastic[6,10] = e
  plastic[5,10] = e

  fR, fG, fB, fX = e
  fRBG=str(fR+20)
  fRBG+=', '
  fRBG+=str(fG+20)
  fRBG+=', '
  fRBG+=str(fB+20)
  f = eval(fRBG)

  plastic[6,3] = f
  plastic[7,3] = f
  plastic[8,3] = f
  plastic[4,4] = f
  plastic[5,4] = f
  plastic[6,4] = f
  plastic[7,4] = f
  plastic[8,4] = f
  plastic[9,4] = f
  plastic[4,5] = f
  plastic[5,5] = f
  plastic[6,5] = f
  plastic[7,5] = f
  plastic[8,5] = f
  plastic[9,5] = f
  plastic[4,6] = f
  plastic[5,6] = f
  plastic[6,6] = f
  plastic[7,6] = f
  plastic[8,6] = f
  plastic[9,6] = f
  plastic[4,7] = f
  plastic[5,7] = f
  plastic[6,7] = f
  plastic[7,7] = f
  plastic[8,7] = f
  plastic[5,8] = f
  plastic[6,8] = f
  plastic[7,8] = f
  
  gR, gG, gB, gX = e
  xx = 230-gR
  gRBG=str(gR+xx)
  gRBG+=', '
  gRBG+=str(gG+xx)
  gRBG+=', '
  gRBG+=str(gB+xx)
  g = eval(gRBG)
  
  plastic[5,5] = g
  plastic[6,5] = g
  plastic[5,6] = g
  
  plasticIm.save(plasticname)
