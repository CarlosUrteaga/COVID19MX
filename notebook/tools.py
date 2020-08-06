from constants import ENTIDADES, MUNICIPIOS, NACIONALIDAD, ORIGEN, RESULTADO, SECTOR, SEXO, SI_NO, TIPO_PACIENTE
import pandas as pd
def replace_all_fields(df):
    df.replace({'ORIGEN': ORIGEN},inplace=True)
    df.replace({"SECTOR": SECTOR},inplace=True)
    df.replace({"SEXO": SEXO},inplace=True)
    df.replace({"TIPO_PACIENTE": TIPO_PACIENTE},inplace=True)
    df.replace({'INTUBADO': SI_NO},inplace=True)
    df.replace({'NEUMONIA': SI_NO},inplace=True)
    df.replace({'NACIONALIDAD': NACIONALIDAD},inplace=True)
    df.replace({'EMBARAZO': SI_NO},inplace=True)
    df.replace({'HABLA_LENGUA_INDIG': SI_NO},inplace=True)
    df.replace({'DIABETES': SI_NO},inplace=True)
    df.replace({'EPOC': SI_NO},inplace=True)
    df.replace({'ASMA': SI_NO},inplace=True)
    df.replace({'INMUSUPR': SI_NO},inplace=True)
    df.replace({'HIPERTENSION': SI_NO},inplace=True)
    df.replace({'OTRA_COM': SI_NO},inplace=True)
    df.replace({'CARDIOVASCULAR': SI_NO},inplace=True)
    df.replace({'OBESIDAD': SI_NO},inplace=True)
    df.replace({'RENAL_CRONICA': SI_NO},inplace=True)
    df.replace({'TABAQUISMO': SI_NO},inplace=True)
    df.replace({'OTRO_CASO': SI_NO},inplace=True)
    df.replace({'RESULTADO': RESULTADO},inplace=True)
    df.replace({'MIGRANTE': SI_NO},inplace=True)
    df.replace({'UCI': SI_NO},inplace=True)
    df.replace({"ENTIDAD_UM": ENTIDADES},inplace=True)
    df.replace({"ENTIDAD_NAC": ENTIDADES},inplace=True)
    df.replace({"ENTIDAD_RES": ENTIDADES},inplace=True)
    df['MUNICIPIO']= df['ENTIDAD_RES'] + df['MUNICIPIO_RES']
    df.replace({"MUNICIPIO": MUNICIPIOS},inplace=True)
    df['MUNICIPIO_RES'] = df['MUNICIPIO'].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
    del df['MUNICIPIO']

def apply_to_report(df):
    df['MUNICIPIO']= df['ENTIDAD_RES'] + df['MUNICIPIO_RES']
    df.replace({'RESULTADO': RESULTADO},inplace=True)
    df.replace({"ENTIDAD_UM": ENTIDADES},inplace=True)
    df.replace({"ENTIDAD_NAC": ENTIDADES},inplace=True)
    df.replace({"ENTIDAD_RES": ENTIDADES},inplace=True)
    df.replace({"MUNICIPIO": MUNICIPIOS},inplace=True)
    df['MUNICIPIO_RES'] = df['MUNICIPIO'].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
    del df['MUNICIPIO']

def to_datetime_df(df):
    df.FECHA_INGRESO = pd.to_datetime(df['FECHA_INGRESO'],)
    df.FECHA_SINTOMAS = pd.to_datetime(df['FECHA_SINTOMAS'],)
    df.FECHA_INGRESO = pd.to_datetime(df['FECHA_INGRESO'],)
    df.loc[df.FECHA_DEF=='9999-99-99', 'FECHA_DEF'] = '2050-12-31'
    df.FECHA_DEF = pd.to_datetime(df['FECHA_DEF'],)

def summary(df):
    return [df.FECHA_ACTUALIZACION.unique()[0]
           ,df[(df.deltaSintomas<14)& (df.RESULTADO=='Positivo SARS-CoV-2')]['ID_REGISTRO'].count()
           ,df[df.RESULTADO=='Positivo SARS-CoV-2']['ID_REGISTRO'].count()
           ,df[(df.FECHA_DEF!='2050-12-31')&(df.RESULTADO=='Positivo SARS-CoV-2')]['ID_REGISTRO'].count()
           ,df[df.RESULTADO=='Resultado pendiente']['ID_REGISTRO'].count()
           ,df.ID_REGISTRO.nunique()
       ,len(df[(df.deltaSintomas<14)& (df.RESULTADO=='Resultado pendiente')])
       ,len(df[(df.FECHA_DEF<'2020-12-31')&(df.RESULTADO=='Resultado pendiente')])
       ,len(df[(df.FECHA_DEF<'2020-12-31')&(df.RESULTADO=='No positivo SARS-CoV-2')])
           ]

def get_deltas_proportion(df):
    column = df.columns[1:]
    for each in column:
        column_name = '∆ '+ each
        df[column_name] = df[each] - df[each].shift(-1)
        column_name1 = '% '+ each
        df[column_name1] = (df[column_name]/ df[column_name].shift(-1))*100