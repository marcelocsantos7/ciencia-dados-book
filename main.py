import pandas as pd

cidades = pd.DataFrame(
    [
        ['Paraná', 'Londrina', 575377, 1356.00],
        ['São Paulo', 'São Carlos', 254484, 1508.00],
        ['Santa Catarina', 'Florianópolis', 508826, 1798.00],
        ['Paraná', 'Curitiba', 1963726, 2293.00],
        ['São Paulo', 'Campinas', 1223237, 1710.00],
    ], columns=['Estado', 'Cidade', 'Habitantes', 'Salário-Médio']
)