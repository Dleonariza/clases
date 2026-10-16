"""
14. Cierre de una feria con ventas electrónicas y reparto
Caso. Un grupo de socios vende sándwiches y jugos en una feria. Ingrese, para cada uno de estos dos
productos, las unidades preparadas, las unidades que no se vendieron, el precio de venta y el costo de
preparación unitario. Ingrese también los gastos fijos, el porcentaje del ingreso cobrado por una
plataforma electrónica, la comisión porcentual de esa plataforma, el porcentaje del excedente que se
destina a un fondo comunitario y el número de socios. La comisión solo afecta la parte del ingreso
recibida por la plataforma. Los productos no vendidos no generan ingresos ni se recupera su costo de
preparación. Muestre las unidades vendidas de cada producto, el ingreso, el costo total de preparación,
la comisión, el excedente, el aporte al fondo y la cantidad que recibe cada socio por partes iguales. Los
datos garantizan un excedente positivo, unidades no vendidas que no superan las preparadas y al menos
un socio.

Entrada
    Sandwiches preparados
    Sandwiches no vendidos
    Precio venta de sandwich
    Costo de preparación de cada sandwich
    Jugos preparados
    Jugos no vendidos
    Precio de venta de jugo
    Costo de preparación de cada jugo
    Gastos fijos
    Porcentaje de ingreso cobrado por plataforma
    Porcentaje comisión
    Porcentaje para el fondo comunitario
    Socios
Proceso
    A los sandwiches preparados se les resta los no vendidos y asi se obtienen los sandwiches vendidos
    A los jugos preparados se les resta los no vendidos y asi se obtienen los jugos vendidos
    El ingreso es los sandwiches vendidos por su precio mas los jugos vendidos por su precio
    El costo de preparacion es los sandwiches preparados por su costo mas los jugos preparados por su costo
    (se usan los preparados porque lo que no se vendio igual se gasto y no se recupera)
    Se saca la parte del ingreso que llego por la plataforma, multiplicando el ingreso por el porcentaje dividido entre 100
    La comision es esa parte de la plataforma multiplicada por el porcentaje de comision dividido entre 100
    El excedente es el ingreso menos el costo de preparacion, menos los gastos fijos y menos la comision
    El aporte al fondo es el excedente multiplicado por el porcentaje del fondo dividido entre 100
    Al excedente se le quita el aporte al fondo y lo que queda se divide entre el numero de socios
Salida
    Sandwiches vendidos
    Jugos vendidos
    Ingreso
    Costo total de preparacion
    Comision
    Excedente
    Aporte al fondo
    Lo que recibe cada socio
"""
sandwiches_preparados = int(input("Sándwiches preparados: "))
sandwiches_no_vendidos = int(input("Sándwiches no vendidos: "))
precio_sandwich = float(input("Precio de venta del sándwich: "))
costo_sandwich = float(input("Costo de preparación unitario del sándwich: "))

jugos_preparados = int(input("Jugos preparados: "))
jugos_no_vendidos = int(input("Jugos no vendidos: "))
precio_jugo = float(input("Precio de venta del jugo: "))
costo_jugo = float(input("Costo de preparación unitario del jugo: "))

gastos_fijos = float(input("Gastos fijos: "))
porcentaje_electronico = float(input("Porcentaje del ingreso cobrado por plataforma electrónica: "))
porcentaje_comision = float(input("Porcentaje de comisión de la plataforma: "))
porcentaje_fondo = float(input("Porcentaje del excedente para el fondo comunitario: "))
socios = int(input("Número de socios: "))

sandwiches_vendidos = sandwiches_preparados - sandwiches_no_vendidos
jugos_vendidos = jugos_preparados - jugos_no_vendidos

ingreso = sandwiches_vendidos * precio_sandwich + jugos_vendidos * precio_jugo
preparacion = sandwiches_preparados * costo_sandwich + jugos_preparados * costo_jugo
cobro_electronico = ingreso * porcentaje_electronico / 100
comision = cobro_electronico * porcentaje_comision / 100
excedente = ingreso - preparacion - gastos_fijos - comision
fondo = excedente * porcentaje_fondo / 100
reparto_por_socio = (excedente - fondo) / socios

print("Sándwiches vendidos:", sandwiches_vendidos)
print("Jugos vendidos:", jugos_vendidos)
print("Ingreso:", ingreso)
print("Costo total de preparación:", preparacion)
print("Comisión:", comision)
print("Excedente:", excedente)
print("Aporte al fondo:", fondo)
print("Reparto por socio:", reparto_por_socio)

