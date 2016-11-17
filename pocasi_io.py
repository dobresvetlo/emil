from sys import version_info
import datetime
import pyowm
import pyowm
API_key = '30c30a1a486c0359e12da3320b60cb45'
owm = pyowm.OWM(API_key, language='cz')

current_time = datetime.datetime.now().time()
hour = (current_time.hour)

#settings for if no input
cast_dne = 'Ahoj'
osloveni = 'pane'
prijmeni = 'Bezprizorny'

py3 = version_info[0] >2

if py3:
  prijmeni = input('Jak se jmenujete prjmenim, prosim? ')
else:
  prijmeni = raw_input('Jak se jmenujete prjmenim, prosim? ')

if py3:
  pohlavi = input('Jste muz, pani, ci slecna? (M = muz, P = pani, S = slecna)')
else:
  pohlavi = raw_input('Jste muz, pani, ci slecna? (M = muz, P = pani, S = slecna)')

if py3:
  misto = input('Kde se prave nachazite? (B = Brno, L = Lucembursko, Vs = Vsetin, Va = Vancouver, P = Praha)')
else:
  misto = raw_input('Kde se prave nachazite? (B = Brno, L = Lucembursko, Vs = Vsetin, Va = Vancouver, P = Praha)')

if (5 <= hour < 10):
	cast_dne = 'Dobre rano'
if (10 <= hour < 12):
	cast_dne = 'Dobre dopoledne'
if (12 <= hour < 17):
	cast_dne = 'Dobre odpoledne'
if (17<= hour < 18):
	cast_dne = 'Dobry podvecer'
if (18<= hour <22):
	cast_dne = 'Dobry vecer'
if (22<= hour <24):
	cast_dne = 'Dobrou noc'
if (hour <5):
	cast_dne = 'Bezte spat'

if (pohlavi == 'M'):
	osloveni = 'pane'
if (pohlavi == 'P'):
	osloveni = 'pani'
if (pohlavi == 'S'):
	osloveni = 'slecno'

if (hour <5 ):	
	zdravim = cast_dne + ' ' + osloveni + ' '+ prijmeni +', vy suvo!'
else:
	zdravim = cast_dne + ' ' + osloveni + ' '+ prijmeni

print(zdravim)
cas = 'Mistni cas je: ' +str(current_time)
print(cas)

if (misto == 'B'):
	lok = 'Brno,Cz'
	in_lok = 'V Brne'
if (misto == 'L'):
	lok = 'Luxembourg'
	in_lok = 'V Lucembursku'
if (misto == 'Vs'):
	lok = 'Vsetin,Cz'
	in_lok = 'Na Vsetine'
if (misto == 'P'):
	lok = 'Praha,Cz'
	in_lok = 'V Pragu'
if (misto == 'Va'):
	lok = 'Vancouver,Can'
	in_lok = 'Ve Vancouveru'

obs = owm.weather_at_place(lok)
poc_ted = obs.get_weather()
teplota = poc_ted.get_temperature()
teplota_v_K = teplota.get('temp')
teplota_v_C = teplota_v_K - 273.15
teplota_v_C = round(teplota_v_C,2)
prsi = poc_ted.get_rain()
clouds = poc_ted.get_clouds()

if prsi == {}:
	rain_status = 'Neprsi.'
else:
	rain_status = 'Prsi'

print(in_lok + ' je momentalne ' + str(teplota_v_C) + ' stupnu.')
print('Oblacno je na ' + str(clouds) + ' procent')
print(rain_status)



