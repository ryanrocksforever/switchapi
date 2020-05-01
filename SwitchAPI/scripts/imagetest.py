import Algorithmia

input = [
    74,
    65,
    42
]
client = Algorithmia.client('simRSafgzh2GEFTlUt9kdSPOg5U1')
algo = client.algo('wilsonmar/RGB2ColorName/0.1.23')
algo.set_options(timeout=300) # optional
print(algo.pipe(input).result)
