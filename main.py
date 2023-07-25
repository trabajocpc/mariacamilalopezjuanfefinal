import pandas as pd
from data.platos import platosPopulares
from data.creartabla import crearTabla

from data.reservas import reservas

from data.proveedores import proveedores

tablaPlatos=pd.DataFrame(platosPopulares)
print(tablaPlatos)
crearTabla(tablaPlatos, "tablaplatospopulares")

tablaReservas=pd.DataFrame(reservas)
print(reservas)
crearTabla(tablaReservas, "tablareservas")

tablaProveedores=pd.DataFrame(proveedores)
print(proveedores)
crearTabla(tablaProveedores, "tablaproveedores")