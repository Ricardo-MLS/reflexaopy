import math
import numpy as np
import matplotlib.pyplot as plt


# usuario insere angulo em graus
degrees1= float(input('digite o angulo de inclinação do espelho 1 em graus:'))

# funcao if para interpretar um angulo agudo
if degrees1 < 90 :
    degrees1 = degrees1
else:
    degrees1 = 180 - degrees1
    
# converter para rad por causa das funcoes trigonometricas
x=math.radians(degrees1)

# matriz A - Primeira transformação relativa a primeira reflexão
A= np.array([[math.cos(2*x), math.sin(2*x)],
             [math.sin(2*x), -1*math.cos(2*x)]])

             
# usuario insere algulo do espelho 2 em graus
degrees2= float(input('digite o angulo de inclinação do espelho 2:'))

# função if para interpretar sempre um angulo obtuso
if degrees2 > 90 :
    degrees2 = degrees2
else:
    degrees2 = 180 - degrees2

# coversao
y= math.radians(degrees2) 


# matriz B- segunda transformação relativa a segunda reflexão
B= np.array([[math.cos(2*y), math.sin(2*y)],
             [math.sin(2*y), -1*math.cos(2*y)]])


#multiplicacao das matrizes BxA para efetuar as transformações 
C= B@A


# variavel a nos aponta para direção em x sempre positiva para o vetor estar incidindo
a= float(input('componente da direção em x(+) do vetor do raio de luz:'))


if a > 0 :
    a = a
else:
    a = -a


# variavel em y sempre negativa para incidir
b= float(input('componente da direção em y(-) do vetor do raio de luz:'))


if b < 0 :
    b = b
else:
    b = -1*b


# matriz coluna que representa as direções do vetor-raio de luz que incide
# sobre o espelho 1
D= np.array([[a],[b]])


#matriz que representa a direção do ultimo vetor refletido 
E= C@D


h= E[0] # elemento 11 da matriz E- direção x do ultimo vetor refletido
f= E[-1] # elemento 12 da matriz E- direção y do ultimo vetor refletido

s= f'a direção do ultimo vetor refletido é: ( {h} , {f} )'
print(s)


c= a*(math.cos(2*x))+ b*(math.sin(2*x)) # direção em x do segundo vetor
d= a*(math.sin(2*x)) - b*(math.cos(2*x)) # direção em y do segundo vetor


mod= (c*c + d*d)**0.5 # norma do vetor 2
m1= math.tan(y)
m2= d/c # coeficiente angular da reta em direção a vec2

# ponto de intersecção com a reta em direção a v2 e a reta do espelho 2 em x
p1= (m1*(-70))/(m2-m1)
# ponto de intersecção com a reta em direção a v2 e a reta do espelho 2 em y
p2= (m1*m2*(-70))/ (m2-m1)


dist= (p1*p1 + p2*p2)**0.5 # distancia da origem até o ponto de intersec


c= c/ mod # vetor unitario c
d= d/ mod # vetor unitario d


c= c* dist # para que c toque com sua extremidade no espelho
d= d* dist # '' d toque ''

n= f'a direção do segundo vetor refletido é: ( {c} , {d} )'
print(n)

def draw(vec1, vec2, vec3): # para plotar os 3 vetores
    '''
    Funcao que plota os 3 vetores.
    
    Primeiro, e criado um array com todos os parametros que serao usados.
    
    Depois, o conteudo desse array e parcialmente separado em 4 variaveis que
    serao usadas na funcao quiver, que gera a imagem do vetor.
    
    Ai, o grafico e gerado com os eixos x e y e seus respectivos limites.
    
    Por fim, as retas e a legenda são gerados e o grafico e exibido.
    '''
    
    array = np.array([[-6*a, -6*b, vec1[0], vec1[1]], 
                      [0, 0, vec2[0], vec2[1]], 
                      [vec2[0], vec2[1], vec3[0], vec3[1]]])
                      
    X, Y, U, V = zip(*array)
    plt.figure()
    plt.ylabel('Eixo Y')
    plt.xlabel('Eixo X')
    ax = plt.gca()
    ax.quiver(X, Y, U, V,color='b', angles='xy', scale_units='xy',scale=1)
    ax.set_xlim([-400, 300])
    ax.set_ylim([-400, 400])
    
    x1= np.arange(-400,300,1)
    plt.plot(x1,x1*(math.tan(x)), label= 'Espelho 1')
    x2= np.arange(-400,300,1)
    plt.plot(x2, m1*(x2-70), label= 'Espelho 2')
    plt.legend(bbox_to_anchor=(0.,1.02, 1., .102), loc= 'lower left', ncol= 2, mode = 'expand', borderaxespad=0.)
    plt.draw()
    plt.show()

# chama e executa a funcao
draw([6*a,6*b], [c,d],[19*h,19*f])