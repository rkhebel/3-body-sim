class System:
    def __init__(self, width, height, masses):
        self.width = width
        self.height = height
        self.masses = masses
        
    def update(self, dt):
        for mass in self.masses:
            net_force_x, net_force_y = 0, 0
            for other_mass in self.masses:
                if mass != other_mass:
                    force_x, force_y = mass.compute_grav_force(other_mass)
                    net_force_x += force_x
                    net_force_y += force_y
            
            # Update the mass's velocity based on net force
            mass.vx += (net_force_x / mass.mass) * dt
            mass.vy += (net_force_y / mass.mass) * dt
            mass.update(dt)
