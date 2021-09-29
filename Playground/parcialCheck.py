boletin = {'materia':['contabilidad','circuitos','literatura'], 'nota':[2.5,3.5,3.3]}
print('La nota en {materia[2]} es {nota[2]}'.format(**boletin))
print('La nota en {materia[2]} es {nota[2]}'.format(materia=boletin['materia'], nota=boletin['nota']))