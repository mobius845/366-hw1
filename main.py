finished = False
while(not(finished)):
  j = input("Enter hex code (type 'q' to quit): ")
  if(j[0] == 'q'):
    finished = True
  else:
    h = int(j, 16)
    h = bin(h)
    h = h[2:]
    h = h.zfill(8)
    print(f'Binary: {h:>30}')
    
    reg = int(h[2:4], base = 2)
    reg2 = int(h[4:6], base = 2)
    reg3 = int(h[6:], base = 2)
    num = int(h[4:], base = 2)
    
    if(h[0:2] == '00'):
      asm = f'init r{reg}, {num}'
      print(f'Assembly: {asm:>30}\n')
    elif(h[0:2] == '01'):
      asm = f'inc r{reg}, {num}'
      print(f'Assembly: {asm:>30}\n')
    else:
      asm = f'add r{reg}, r{reg2}, r{reg3}'
      print(f'Assembly: {asm:>30}\n')
