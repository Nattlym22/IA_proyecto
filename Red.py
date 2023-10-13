from pomegranate import *
import networkx as nx
import matplotlib.pyplot as plt
from colorama import Style, Fore, Back

# Nodo Edad
edad = Node(DiscreteDistribution({
    "joven": 0.3,
    "adulto joven": 0.4,
    "adulto mayor": 0.3
}), name="edad")

# Nodo Género
genero = Node(DiscreteDistribution({
    "masculino": 0.5,
    "femenino": 0.5
}), name="genero")

# Nodo Estatura (depende del género)
estatura = Node(ConditionalProbabilityTable([
    ["masculino", "baja", 0.1],
    ["masculino", "promedio", 0.6],
    ["masculino", "alta", 0.3],
    ["femenino", "baja", 0.2],
    ["femenino", "promedio", 0.7],
    ["femenino", "alta", 0.1],
], [genero.distribution]), name="estatura")

# Nodo Contextura (depende de edad y estatura)
contextura = Node(ConditionalProbabilityTable([
    ["joven", "baja", "delgado", 0.2],
    ["joven", "baja", "promedio", 0.6],
    ["joven", "baja", "robusto", 0.2],
    ["joven", "promedio", "delgado", 0.3],
    ["joven", "promedio", "promedio", 0.5],
    ["joven", "promedio", "robusto", 0.2],
    ["joven", "alta", "delgado", 0.1],
    ["joven", "alta", "promedio", 0.3],
    ["joven", "alta", "robusto", 0.6],
    ["adulto joven", "baja", "delgado", 0.2],
    ["adulto joven", "baja", "promedio", 0.5],
    ["adulto joven", "baja", "robusto", 0.3],
    ["adulto joven", "promedio", "delgado", 0.3],
    ["adulto joven", "promedio", "promedio", 0.4],
    ["adulto joven", "promedio", "robusto", 0.3],
    ["adulto joven", "alta", "delgado", 0.1],
    ["adulto joven", "alta", "promedio", 0.4],
    ["adulto joven", "alta", "robusto", 0.5],
    ["adulto mayor", "baja", "delgado", 0.1],
    ["adulto mayor", "baja", "promedio", 0.4],
    ["adulto mayor", "baja", "robusto", 0.5],
    ["adulto mayor", "promedio", "delgado", 0.2],
    ["adulto mayor", "promedio", "promedio", 0.4],
    ["adulto mayor", "promedio", "robusto", 0.4],
    ["adulto mayor", "alta", "delgado", 0.1],
    ["adulto mayor", "alta", "promedio", 0.3],
    ["adulto mayor", "alta", "robusto", 0.6],
    # Otras combinaciones de edad, estatura y contextura
], [edad.distribution, estatura.distribution]), name="contextura")


# Nodo Estado Civil (depende de la edad)
# Nodo Estado Civil (depende de la edad)
estado_civil = Node(ConditionalProbabilityTable([
    ["joven", "soltero", 0.5],
    ["joven", "casado", 0.2],
    ["joven", "divorciado", 0.2],
    ["joven", "viudo", 0.1],  # Agregar "viudo" como un estado válido
    ["adulto joven", "soltero", 0.4],
    ["adulto joven", "casado", 0.3],
    ["adulto joven", "divorciado", 0.2],
    ["adulto joven", "viudo", 0.1],  # Agregar "viudo" como un estado válido
    ["adulto mayor", "soltero", 0.1],
    ["adulto mayor", "casado", 0.5],
    ["adulto mayor", "divorciado", 0.3],
    ["adulto mayor", "viudo", 0.1],  # Agregar "viudo" como un estado válido
], [edad.distribution]), name="estado_civil")



# Nodo Orientación Sexual (depende del género)
orientacion_sexual = Node(ConditionalProbabilityTable([
    ["masculino", "heterosexual", 0.6],
    ["masculino", "homosexual", 0.2],
    ["masculino", "bisexual", 0.2],
    ["femenino", "heterosexual", 0.7],
    ["femenino", "homosexual", 0.1],
    ["femenino", "bisexual", 0.2],
], [genero.distribution]), name="orientacion_sexual")

# Nodo Nivel Académico (depende de género y orientación sexual)
nivel_academico = Node(ConditionalProbabilityTable([
    ["masculino", "heterosexual", "no presenta", 0.1],
    ["masculino", "heterosexual", "primaria", 0.2],
    ["masculino", "heterosexual", "secundaria", 0.4],
    ["masculino", "heterosexual", "superior", 0.3],
    ["masculino", "homosexual", "no presenta", 0.2],
    ["masculino", "homosexual", "primaria", 0.1],
    ["masculino", "homosexual", "secundaria", 0.4],
    ["masculino", "homosexual", "superior", 0.3],
    ["masculino", "bisexual", "no presenta", 0.15],
    ["masculino", "bisexual", "primaria", 0.2],
    ["masculino", "bisexual", "secundaria", 0.35],
    ["masculino", "bisexual", "superior", 0.3],
    ["femenino", "heterosexual", "no presenta", 0.05],
    ["femenino", "heterosexual", "primaria", 0.15],
    ["femenino", "heterosexual", "secundaria", 0.5],
    ["femenino", "heterosexual", "superior", 0.3],
    ["femenino", "homosexual", "no presenta", 0.1],
    ["femenino", "homosexual", "primaria", 0.1],
    ["femenino", "homosexual", "secundaria", 0.5],
    ["femenino", "homosexual", "superior", 0.3],
    ["femenino", "bisexual", "no presenta", 0.1],
    ["femenino", "bisexual", "primaria", 0.15],
    ["femenino", "bisexual", "secundaria", 0.4],
    ["femenino", "bisexual", "superior", 0.35],
    # Otras combinaciones de género, orientación sexual y nivel académico
], [genero.distribution, orientacion_sexual.distribution]), name="nivel_academico")

# Nodo Compatibilidad (depende de estado civil y nivel académico)
compatibilidad = Node(ConditionalProbabilityTable([
    ["soltero", "no presenta", "sí", 0.9],
    ["soltero", "no presenta", "no", 0.1],
    ["soltero", "primaria", "sí", 0.7],
    ["soltero", "primaria", "no", 0.3],
    ["soltero", "secundaria", "sí", 0.8],
    ["soltero", "secundaria", "no", 0.2],
    ["soltero", "superior", "sí", 0.6],
    ["soltero", "superior", "no", 0.4],
    ["casado", "no presenta", "sí", 0.7],
    ["casado", "no presenta", "no", 0.3],
    ["casado", "primaria", "sí", 0.6],
    ["casado", "primaria", "no", 0.4],
    ["casado", "secundaria", "sí", 0.8],
    ["casado", "secundaria", "no", 0.2],
    ["casado", "superior", "sí", 0.5],
    ["casado", "superior", "no", 0.5],
    ["divorciado", "no presenta", "sí", 0.6],
    ["divorciado", "no presenta", "no", 0.4],
    ["divorciado", "primaria", "sí", 0.5],
    ["divorciado", "primaria", "no", 0.5],
    ["divorciado", "secundaria", "sí", 0.7],
    ["divorciado", "secundaria", "no", 0.3],
    ["divorciado", "superior", "sí", 0.4],
    ["divorciado", "superior", "no", 0.6],
    ["viudo", "no presenta", "sí", 0.9],
    ["viudo", "no presenta", "no", 0.1],
    ["viudo", "primaria", "sí", 0.8],
    ["viudo", "primaria", "no", 0.2],
    ["viudo", "secundaria", "sí", 0.7],
    ["viudo", "secundaria", "no", 0.3],
    ["viudo", "superior", "sí", 0.6],
    ["viudo", "superior", "no", 0.4],
    # Otras combinaciones de estado civil, nivel académico y compatibilidad
], [estado_civil.distribution, nivel_academico.distribution]), name="compatibilidad")

# Crear una Red Bayesiana y añadir estados y bordes
modelo = BayesianNetwork()
modelo.add_states(edad, genero, estatura, contextura, estado_civil, orientacion_sexual, nivel_academico, compatibilidad)


modelo.add_edge(edad, estado_civil)
modelo.add_edge(genero, estatura)
modelo.add_edge(estatura, contextura)
modelo.add_edge(edad, contextura)
modelo.add_edge(genero, orientacion_sexual)
modelo.add_edge(genero, nivel_academico)
modelo.add_edge(orientacion_sexual, nivel_academico)
modelo.add_edge(estado_civil, compatibilidad)
modelo.add_edge(nivel_academico, compatibilidad)

# Compilar el modelo
modelo.bake()
if __name__ == "__main__":
    # Crear una representación de la Red Bayesiana como un objeto DiGraph
    red_bayesiana = nx.DiGraph()

    # Agregamos nodos a la representación de la red
    for node in modelo.states:
        red_bayesiana.add_node(node.name)

    # Agregamos bordes a la representación de la red
    for edge in modelo.edges:
        red_bayesiana.add_edge(edge[0].name, edge[1].name)

    # Visualizar la estructura de la red
    pos = nx.spring_layout(red_bayesiana, seed=42)
    labels = {node: node for node in red_bayesiana.nodes()}
    nx.draw(red_bayesiana, pos, labels=labels, with_labels=True, node_size=5000, node_color="magenta")
    plt.title("Estructura de la Red Bayesiana")
    plt.show()
 