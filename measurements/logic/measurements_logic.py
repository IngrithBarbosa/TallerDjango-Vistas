from ..models import Measurement
import variables.logic.variables_logic as vl
def getMeasurements():
    measurements= Measurement.objects.all()
    return measurements
def get_measurement(mea_pk):
    measurement= Measurement.objects.get(pk=mea_pk)
    return measurement
def create_measurement(mea):
    measurement = Measurement(variable=vl.get_variable(mea["variable"]),
                             unit=mea["unit"],
                             value=mea["value"],
                             place=mea["place"])
    measurement.save()
    return measurement
def update_measurement(mea_pk, new_mea):
    measurement = get_measurement(mea_pk)
    measurement.variable= vl.get_variable(new_mea["variable"])
    measurement.unit= new_mea["unit"]
    measurement.value= new_mea["value"]
    measurement.place= new_mea["place"]
    measurement.save()
    return measurement
def delete_measurement(mea_pk):
    measurement= get_measurement(mea_pk)
    measurement.delete()

