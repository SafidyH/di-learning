import random

class Gene:
    def __init__(self, value):
        self.value = value
    
    def flip(self):
        self.value = 1 - self.value

class Chromosome:
    def __init__(self):
        self.genes = [Gene(random.randint(0, 1)) for _ in range(10)]
    
    def mutate(self):
        num_flips = random.randint(0, 10)
        for _ in range(num_flips):
            gene = random.choice(self.genes)
            gene.flip()

class DNA:
    def __init__(self):
        self.chromosomes = [Chromosome() for _ in range(10)]
    
    def mutate(self):
        num_flips = random.randint(0, 10)
        for _ in range(num_flips):
            chromosome = random.choice(self.chromosomes)
            chromosome.mutate()

class Organism:
    def __init__(self, dna, environment):
        self.dna = dna
        self.environment = environment
        self.generation = 0
    
    def mutate_until_all_ones(self):
        while not all(gene.value == 1 for chromosome in self.dna.chromosomes for gene in chromosome.genes):
            self.dna.mutate()
            self.generation += 1
            if random.random() < self.environment:
                self.dna.mutate()
                self.generation += 1

# Example usage
dna = DNA()
organism = Organism(dna, 0.1)
organism.mutate_until_all_ones()
print(f"Generations: {organism.generation}")
