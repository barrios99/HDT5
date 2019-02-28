#Albeño, Fátima - 18060
#De León, Diana - 18607

import simpy
import random

v_p=2 #velocidad del procesador
contador_ins = 0
intervalo = 10

def proceso(numero, m_ram, cant_p, space, env):
    inicio=env.now
    random.seed(25)
    espacio = space
    yield m_ram.put(espacio)
    with cpu.request() as turno:
        yield turno
        yield env.timeout(cant_p/v_p)
    print('Pasando el proceso #' +str(i)+' que usa '+ str(espacio) +' de RAM con '+ str(cant_p)+' de instrucciones en %d segundos'%env.now)
    tiempo_trans=env.now-inicio
    print (str(i)+' se tardo %f para el proceso' % (tiempo_trans))
#def prueba(env):
 #   p = env.process(proceso(m_ram,cant_procesos,cpu,env))
  #  yield p

env = simpy.Environment()
#Crear la memoria RAM, capacidad maxima 100
m_ram = simpy.Container(env, init=100)
cpu = simpy.Resource(env, capacity = 1)
def create(numero, m_ram, cant_p, space, env):
    yield env.timeout(random.expovariate(1 / 0.5))
    env.process(proceso(numero,m_ram, int(random.expovariate(1.0/intervalo)),random.randint(1,10),env))

for i in range(25):
    env.process(create(i,m_ram, int(random.expovariate(1.0/intervalo)),random.randint(1,10),env))  
env.run()



