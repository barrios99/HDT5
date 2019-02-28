#Albeño, Fátima - 18060
#De León, Diana - 18607

import collections
import simpy
import random
import statistics as stats

contador_ins = 0

def proceso(m_ram, cant_p, espacio, env):
    global tiempo_procesos
    inicio=env.now
    yield m_ram.put(espacio)
    with cpu.request() as turno:
        yield turno
        if cant_p<3:
            cant=cant_p
        else:
            cant_p-=3
            cant=3
        yield env.timeout(cant)
        yield m_ram.get(espacio)
    print('Pasando el proceso que usa '+ str(espacio) +' de RAM con '+ str(cant_p)+' de instrucciones en %d segundos'%env.now)
    tiempo_trans=env.now-inicio
    print ('se tardo %f para el proceso' % (tiempo_trans))
    tiempo_procesos.append(tiempo_trans)

def ready_p(m_ram, cant_p, espacio, env):
    

def create(m_ram, cant_p, space, env):
    yield env.timeout(random.expovariate(1.0 / 10))
    env.process(proceso(m_ram, cant_p, space, env))

Proceso=collections.namedtuple('Proceso','ram, instrucciones')

env = simpy.Environment()
#Crear la memoria RAM, capacidad maxima 100
m_ram = simpy.Container(env, init=0, capacity=100)
ready=simpy.Store(env)
cpu = simpy.Resource(env, capacity = 1)
tiempo_procesos=[]
random.seed(25)
for i in range(25):
    env.process(create(m_ram,random.randint(1,10),random.randint(1,10),env))  
env.run()
print ("tiempo promedio por proceso es: ", stats.mean(tiempo_procesos))
print ("la desviacion estandar es: ", stats.pstdev(tiempo_procesos))


