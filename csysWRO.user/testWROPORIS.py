from csysWROPORIS import *

model = csysWROPORIS()

# Mostramos información del modelo
print("Nombre de modelo:",model.root.name)
print("Modos disponibles:",model.root.modes)

# Seleccionamos el modo de misión Normal
model.root.setMode(model.mdMisionMode_Normal)
print("\n\n\nModo actual de la misión:",model.root.selectedMode.name)
print("Tramos disponibles:",model.sysTramo.modes)

# Seleccionamos el tramo P00
model.sysTramo.setMode(model.mdTramoMode_P00_SituarBNB_finBNB_Avanzar)
print("\n\n\nTramo actual:",model.sysTramo.selectedMode.name)
print("Situación actual:",model.sysSituacion.selectedMode.name)
print("Decisión actual movilidad:",model.sysDecisionMovimiento.selectedMode.name)
print("Decisión actual aparejo:",model.sysDecisionAparejo.selectedMode.name)
print("Decisión actual siguiente paso:",model.sysNuevoPaso.selectedMode.name)
print("Ruedas: ",model.prRuedaDer.selectedValue.name,model.prRuedaIzq.selectedValue.name)

# Seleccionamos el tramo P01
model.sysTramo.setMode(model.mdTramoMode_P01_SeguirBNB_finder_giroder_abrir)
print("\n\n\nTramo actual:",model.sysTramo.selectedMode.name)
print("Situación actual:",model.sysSituacion.selectedMode.name)
print("Decisión actual movilidad:",model.sysDecisionMovimiento.selectedMode.name)
print("Decisión actual aparejo:",model.sysDecisionAparejo.selectedMode.name)
print("Decisión actual siguiente paso:",model.sysNuevoPaso.selectedMode.name)
print("Ruedas: ",model.prRuedaDer.selectedValue.name,model.prRuedaIzq.selectedValue.name)

# Seleccionamos el tramo P07
model.sysTramo.setMode(model.mdTramoMode_P07_SituarVVB_finVVB_Avanzar)
print("\n\n\nTramo actual:",model.sysTramo.selectedMode.name)
print("Situación actual:",model.sysSituacion.selectedMode.name)
print("Decisión actual movilidad:",model.sysDecisionMovimiento.selectedMode.name)
print("Decisión actual aparejo:",model.sysDecisionAparejo.selectedMode.name)
print("Decisión actual siguiente paso:",model.sysNuevoPaso.selectedMode.name)
print("Ruedas: ",model.prRuedaDer.selectedValue.name,model.prRuedaIzq.selectedValue.name)
# Cambiamos la situación
model.sysSituacion.setMode(model.mdSituacionMode_NNN_07)
print("\n\n\nSituación actual:",model.sysSituacion.selectedMode.name)
print("Decisión actual movilidad:",model.sysDecisionMovimiento.selectedMode.name)
print("Decisión actual aparejo:",model.sysDecisionAparejo.selectedMode.name)
print("Decisión actual siguiente paso:",model.sysNuevoPaso.selectedMode.name)
print("Ruedas: ",model.prRuedaDer.selectedValue.name,model.prRuedaIzq.selectedValue.name)
# Cambiamos la situación
model.sysSituacion.setMode(model.mdSituacionMode_VVB_07)
print("\n\n\nSituación actual:",model.sysSituacion.selectedMode.name)
print("Decisión actual movilidad:",model.sysDecisionMovimiento.selectedMode.name)
print("Decisión actual aparejo:",model.sysDecisionAparejo.selectedMode.name)
print("Decisión actual siguiente paso:",model.sysNuevoPaso.selectedMode.name)
print("Ruedas: ",model.prRuedaDer.selectedValue.name,model.prRuedaIzq.selectedValue.name)