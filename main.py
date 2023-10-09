import requests

credentials = '22731753'

s = requests.Session()

proffesors = {}
students = []

def init():


  s.post('http://190.182.49.248:81/sisnota/controlador/ctrLogin.php', data={
  'sw':1,'usuario':'22731753','passw':'22731753','ip':'191.95.143.157','host':'Dinamic-Tigo-191-95-143-157.tigo.com.co','xop':'0'})

  r = s.post('http://190.182.49.248:81/sisnota/controlador/ctrAdmon.php', data={'sw':7,'codDocnt':27,'codCurso':0,'id':0.6044666395715124}).json()
  
  for curso in r:
    proffesors[curso['CODCUR_CAR']] = {'grado': curso['NOMGRA_GRA'],'professor': curso['NOMPRO_CUR'], 'details': curso['DETALLE_CUR']}

def get_names(course, year):

  r2: list = s.post('http://190.182.49.248:81/sisnota/controlador/ctrAdmon.php', data={'sw':15,'codCurso':course,'anio':year}).json()

  r2.pop(0)

  for stu in r2:
    students.append({'cod': stu['CODIGO_AL'],'name': stu['NOMBRE'].replace('  ', ' ')})


def get_pdf(year, course):

  periodo = int(input('Periodo: '))

  name_person = input('Name: ').upper().strip().replace('  ', ' ')

  for k in students:

    temp_name = k['name']

    if name_person in temp_name:
      cod_al = k['cod']
    else:
      pass

  try:
    url_request = f'http://190.182.49.248:81/sisnota/controlador/ctrInformes.php?&sw=1&anioLec={year}&periodo={periodo}&curso={course}&alumno={cod_al}&nomPeriodo=N&nomCurso=N&xnomCurso=N&infBasica=N&op=0'
  except UnboundLocalError:
    exit('\nSTUDENT NOT FOUND\n')


  r3 = s.get(url=url_request)

  with open(f'{name_person}.pdf','wb') as f:
    f.write(r3.content)



if __name__ == '__main__':
  init()

  course = input('Course: ')
  year = input('Year: ')

  get_names(course=course, year=year)
  get_pdf(year=year, course=course)