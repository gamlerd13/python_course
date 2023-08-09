from datetime import datetime
# Este modulo maneja las zonas horarias de todos los lugares del mundo
from pytz import timezone
import pytz

hora_universal = datetime.now(timezone('UTC'))
hora_lima_1 = hora_universal.astimezone(pytz.timezone('America/Lima'))
hora_lima = datetime.now(timezone('America/Lima'))
print(hora_universal)
print(hora_lima_1)
print(hora_lima)


hora_lima2 = pytz.timezone('America/Lima')

fecha = "20:04:25"

tz_lima = pytz.timezone('America/Lima')
fecha_lima = hora_universal.astimezone(tz_lima)
print(fecha_lima)