import pandas as pd

def leer_datos(file):
    """
    Lee un archivo y lo devuelve como un DataFrame
        Args: 
        file(str): Nombre archivo

        Returns:
        pd.DataFrame: DF con los datos del archivo
    """
    
    extension= file.split('.')[-1].lower()

    if extension =='csv':
        return pd.read_csv(file)
    elif extension in ['xls','xlsx']:
        return pd.read_excel(file)
    elif extension == 'json':
        return pd.read_json(file)
    elif extension == 'txt':
        return pd.read_csv(file, delimiter="\t")
    else:
        raise ValueError(f"Formato de archivo no soportado:{extension}")
    

    
def explorar_datos(df):
    """
    Explora un DataFrame y muestra informacion. Numero de filas y columnas, tipos de datos. Valores duplicados

    Arg: 
    df(df.DataFrame)

    Return:
    Información relativa al df.
    """
    print("Muestra de DataFrame")
    display(df.sample(5))
    print(f'\nINFORMACION:\n')
    print(f'Columnas: {df.shape[1]}\nFilas: {df.shape[0]}\n')
    print("Columnas, tipo de datos:\n")
    if df.shape[1]>7:
        display(pd.DataFrame(df.types,columns=["tipo_dato"]))
        print(f'Información resumida\n')
        print(df.info())
    else:
        print(df.info())
    print(f'Valores duplicados:')
    if df.duplicated().sum()== 0:
        print("NO HAY VALORES DUPLICADOS")
    else:
        print(f'Número de valores duplicados {df.duplicated().sum()}')
        print("Los valores duplicados son:\n")
        duplicados=df[df.duplicated()]
        display(duplicados)

def info_duplicados (df):
    """
    Determina el numero de filas duplicadas y las guarda en un DataFrame para su revisión

    args:
    df(pd.DataFrame)
    Returns:
    int: numero de duplicados.
    Float: % de duplicados.
    pd.DataFrame: DataFrame con los duplicados 
    """
    num_duplicados=df.duplicated().sum()
    print(f'El DataFrame presenta {num_duplicados} filas duplicadas')

    duplicados=df[df.duplicated()]
    df_filas_duplicados=pd.DataFrame(duplicados)

    perc_duplicados= round(num_duplicados/df.shape[0] *100,2)
    print(f'El porcentaje de duplicados es de un {perc_duplicados} %.\n')

    return df_filas_duplicados, num_duplicados

def estudio_variables(df, tipo_variable):
    """ 
    Aporta información de los tipos de variables del DataFrame.
    Indica tipo de variables y un análisis estadístico básico
    Args: 
    df(pd.DataFrame)
    tipo_variable (string): Indica el tipo de variable del que se solicita informacion.
    Returns:
    lista con los tipos de valores correspondientes y los DataFrame con las columnas separadas por tipo de variable
    """
    df_categoricas=df.select_dtypes(include='object')
    df_numericas=df.select_dtypes(include=['int','float'])
    print(f'Las variables de tipo {tipo_variable} son:')
    if tipo_variable.lower() =='categoricas':
        columnas_cat=list(df_categoricas.columns)
        print(columnas_cat)
        print(f'\nLas principales estadísticas son:\n')
        display(df_categoricas.describe().T)
    elif tipo_variable.lower() =='numericas':
        columnas_num=list(df_numericas.columns)
        print(columnas_num)
        print(f'\nLas principales estadísticas son:\n')
        display(df_numericas.describe().T)
    else:
        print('Tipo de variable no conocido.')
    return df_categoricas,df_numericas

def valores_unicos_frecuencias(df):
    """ 
    Indica los valores únicos de cada columna en un df
    Args:
    df (pd.DataFrame)
    Returns:
    None.
    """
    for columna in df.columns:
        print(f'\nPara la columna {columna} los valores únicos son:\n')
        print(df[columna].value_counts())

def numero_filas(df,nombre_df):
    """ Devuelve el numero de filas
        Arg (df)
        Return(NONE)
    """
    print(f'Numero de filas de df {nombre_df}: {df.shape[0]} filas')