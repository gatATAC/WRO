from WROPORIS import *

model = WROPORIS()

# Mostramos información del modelo
print("Nombre de modelo:",model.root.name)
print("Modos disponibles:",model.root.modes)

# Seleccionamos el modo de misión Normal
model.root.setMode(model.mdMisionNormal)
print("\n\n\nModo actual de la misión:",model.root.selectedMode.name)
print("Tramos disponibles:",model.sysTramo.modes)

# Seleccionamos el tramo P00
model.sysTramo.setMode(model.mdTramoP00)
print("\n\n\nTramo actual:",model.sysTramo.selectedMode.name)
print("Situación actual:",model.sysSituacion.selectedMode.name)
print("Decisión actual movilidad:",model.sysDecisionMovimiento.selectedMode.name)
print(model.sysDecisionAparejo.modes)
print(model.sysDecisionAparejo.selectedMode)
print("Decisión actual aparejo:",model.sysDecisionAparejo.selectedMode.name)
print(model.sysNuevoPaso.modes)
print(model.sysNuevoPaso.selectedMode)
print("Decisión actual siguiente paso:",model.sysNuevoPaso.selectedMode.name)
print("Ruedas: ",model.prRuedaDer.selectedValue.name,model.prRuedaIzq.selectedValue.name)

# Seleccionamos el tramo P01
model.sysTramo.setMode(model.mdTramoP01)
print("\n\n\nTramo actual:",model.sysTramo.selectedMode.name)
print("Situación actual:",model.sysSituacion.selectedMode.name)
print("Decisión actual movilidad:",model.sysDecisionMovimiento.selectedMode.name)
print("Decisión actual aparejo:",model.sysDecisionAparejo.selectedMode.name)
print("Decisión actual siguiente paso:",model.sysNuevoPaso.selectedMode.name)
print("Ruedas: ",model.prRuedaDer.selectedValue.name,model.prRuedaIzq.selectedValue.name)

# Seleccionamos el tramo P07
model.sysTramo.setMode(model.mdTramoP07)
print("\n\n\nTramo actual:",model.sysTramo.selectedMode.name)
print("Situación actual:",model.sysSituacion.selectedMode.name)
print("Decisión actual movilidad:",model.sysDecisionMovimiento.selectedMode.name)
print("Decisión actual aparejo:",model.sysDecisionAparejo.selectedMode.name)
print("Decisión actual siguiente paso:",model.sysNuevoPaso.selectedMode.name)
print("Ruedas: ",model.prRuedaDer.selectedValue.name,model.prRuedaIzq.selectedValue.name)
# Cambiamos la situación
model.sysSituacion.setMode(model.mdSituacionNNN_07)
print("\n\n\nSituación actual:",model.sysSituacion.selectedMode.name)
print("Decisión actual movilidad:",model.sysDecisionMovimiento.selectedMode.name)
print("Decisión actual aparejo:",model.sysDecisionAparejo.selectedMode.name)
print("Decisión actual siguiente paso:",model.sysNuevoPaso.selectedMode.name)
print("Ruedas: ",model.prRuedaDer.selectedValue.name,model.prRuedaIzq.selectedValue.name)
# Cambiamos la situación
model.sysSituacion.setMode(model.mdSituacionVVB_07)
print("\n\n\nSituación actual:",model.sysSituacion.selectedMode.name)
print("Decisión actual movilidad:",model.sysDecisionMovimiento.selectedMode.name)
print("Decisión actual aparejo:",model.sysDecisionAparejo.selectedMode.name)
print("Decisión actual siguiente paso:",model.sysNuevoPaso.selectedMode.name)
print("Ruedas: ",model.prRuedaDer.selectedValue.name,model.prRuedaIzq.selectedValue.name)