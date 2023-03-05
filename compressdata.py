pointsdata=[
[35.3636111111,68.1777777778,0,227490,"Tala-Barfak Mine, Tala Wa Barfak District, Baghlan, Afghanistan",0,"","1","60"]
,[35.3102777778,68.1005555556,0,227474,"East Eshpushta clay occurrence, Eshpushta, Kahmard District, Bamyan, Afghanistan",0,"","1","281"]
,[35.3013888889,68.0705555556,0,227489,"West Eshpushta clay occurrence, Eshpushta, Kahmard District, Bamyan, Afghanistan",0,"","1","281"]
,[32.899166666667,67.687222222222,0,404930,"Zarkashan Au-Cu deposit, Muqur District, Ghazni, Afghanistan",0,"","1","63"]
,[36.5833333333,69.6166666667,0,227525,"Taqcha Khana clay mine, Taqcha Khana, Namak Ab District, Takhar, Afghanistan",0,"","1","60"]
,[32.3127777778,66.5327777778,0,226422,"Kundalan Cu-polymetallic deposit, Mizan District, Zabul, Afghanistan",0,"","1","56"]
]

def compressdata(pointsdata):
  output = []
  for point in pointsdata:
    output.append([[point[0],point[1]],point[3]])
  return output