#Obtener Sets ordenador por fecha de salida (El ultimo primero)

def lastset():
	return "select * from mtg_schema.sets order by substring(date,4,4) desc,substring(date,1,2) desc"

