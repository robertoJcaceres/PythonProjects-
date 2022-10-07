import json
import string
import sys
import getopt
from datetime import datetime


def RecordEsfigmoTry(Genero, Edad, Peso, DiastolicaTeorica, SiastolicaTeorica, VEsfigmo, NoGrabacion, NoN):

    flag_genero = 0
    flag_Edad = 0
    flag_Peso = 0
    t1 = "Genero correcto"
    t2 = "dad correcta"
    t3 = "Peso correcto"
    t4 = "Version Correcta"

    Genero = str(Genero)
    Edad = int(Edad)
    Peso = float(Peso)
    DiastolicaTeorica = int(DiastolicaTeorica)
    SiastolicaTeorica = int(SiastolicaTeorica)
    VEsfigmo = float(VEsfigmo)

    pulso = [28, 24, 32, 43, 16, 75, 65, 91, 127, 176,
             229, 305, 360, 478, 502, 391, 341, 320, 234]
    presion = [6, 12, 17, 22, 26, 37, 41, 45, 49,
               56, 60, 66, 71, 79, 86, 92, 96, 104, 111]
    A = 0.0247
    B = 0.0478
    alpha = 0.70
    betha = 0.40
    Sistolic = 91
    Diastolic = 70

    if Genero.lower() == "m":
        genero = "male"

    elif Genero.lower() == "f":
        genero = "female"

    else:
        flag_genero = 1
        t1 = "No ingreso genero correcto"

    if Edad < 0 or Edad > 120:
        t2 = "La edad no está en un rango adecuado"
        flag_Edad = 1
    else:
        edad = Edad

    if Peso < 0 or Peso > 400:
        t3 = "Peso no está en un rango adecuado"
        flag_Peso = 1
    else:
        peso = Peso

    if VEsfigmo < 0.0 or VEsfigmo > 20.0:
        t4 = "Version no aceptada"
        flag_vesfigmo = 1
    else:
        Vesfigmo = str(VEsfigmo)

    date = datetime.now().date()
    date = str(date)

    if flag_Peso == 0 and flag_genero == 0 and flag_Edad == 0:
        record = {
            "A": A,
            "B": B,
            "alpha": alpha,
            "betha": betha,
            "pulse": pulso,
            "pressure": presion,
            "Sistolic": Sistolic,
            "Diastolic": Diastolic,
            "Gender": genero,
            "Age": edad,
            "Weight": peso,
            "TheoricalSistolic": SiastolicaTeorica,
            "TheoricalDiastolic": DiastolicaTeorica}
        print(record)
        with open('subject'+'_'+NoN+'_'+'Rec' + NoGrabacion + '_' + 'VEsfigmo'+Vesfigmo + '_' + date+'.json', 'w') as fp:
            json.dump(record, fp)

    elif flag_Edad == 1 or flag_genero == 1 or flag_Peso == 1:
        print(t1 + "," + t2+","+t3 + " " + t4 +
              " "+"Ingrese los datos de nuevo")


RecordEsfigmoTry(sys.argv[1], sys.argv[2],
                 sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8])
