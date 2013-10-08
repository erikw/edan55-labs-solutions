approx = [21, 250, 2242, 21510, 222251, 2539469];
exact = [22, 251, 2228, 21664, 217212, 2168611];

abs((approx - exact) ./ exact)
abs((exact - approx) ./ exact)




