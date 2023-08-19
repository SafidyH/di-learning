import random

class QuantumParticle:
    def __init__(self, x=None, p=None):
        if x is None:
            self.x = self.position()
        else:
            self.x = x

        if p is None:
            self.p = self.momentum()
        else:
            self.p = p

        self.spin_value = self.spin()

    def position(self):
        return random.randint(1, 10000)

    def momentum(self):
        return random.random()

    def spin(self):
        return random.choice([-0.5, 0.5])

    def disturb(self):
        self.x = self.position()
        self.p = self.momentum()
        print("Quantum Interferences!!")

    def entangle(self, other_particle):
        if not isinstance(other_particle, QuantumParticle):
            print("Quantum entanglement can only be with another QuantumParticle!")
        else:
            self.spin_value = -self.spin_value
            other_particle.spin_value = -self.spin_value
            print("Particle {} is now in quantum entanglement with Particle {}".format(self, other_particle))

    def __repr__(self):
        return f"QuantumParticle(x={self.x}, p={self.p}, spin={self.spin_value})"

# Example usage:
p1 = QuantumParticle(x=1, p=5.0)
p2 = QuantumParticle(x=2, p=5.0)
p1.entangle(p2)
