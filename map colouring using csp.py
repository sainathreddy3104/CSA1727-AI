class MapColoringCSP:
    def __init__(self, variables, domains, neighbors):
        """
        Initialize the CSP solver for map coloring.
        
        Args:
            variables (list): List of regions to color (e.g., ['WA', 'NT', 'SA', ...]).
            domains (dict): Possible colors for each variable (e.g., {'WA': ['R', 'G', 'B'], ...}).
            neighbors (dict): Adjacency list (e.g., {'WA': ['NT', 'SA'], ...}).
        """
        self.variables = variables
        self.domains = domains
        self.neighbors = neighbors
        self.assignment = {}

    def is_consistent(self, variable, color):
        """Check if assigning 'color' to 'variable' violates any constraints."""
        for neighbor in self.neighbors[variable]:
            if neighbor in self.assignment and self.assignment[neighbor] == color:
                return False
        return True

    def select_unassigned_variable(self):
        """Select the next unassigned variable using Minimum Remaining Values (MRV) heuristic."""
        unassigned = [v for v in self.variables if v not in self.assignment]
        return min(unassigned, key=lambda v: len(self.domains[v]))

    def order_domain_values(self, variable):
        """Order domain values using Least Constraining Value (LCV) heuristic."""
        return sorted(self.domains[variable], key=lambda color: sum(1 for n in self.neighbors[variable] if color in self.domains[n]))

    def backtracking_search(self):
        """Backtracking search with MRV and LCV heuristics."""
        if len(self.assignment) == len(self.variables):
            return self.assignment  # Solution found

        var = self.select_unassigned_variable()
        for color in self.order_domain_values(var):
            if self.is_consistent(var, color):
                self.assignment[var] = color
                result = self.backtracking_search()
                if result is not None:
                    return result
                del self.assignment[var]  # Backtrack
        return None  # No solution

# Example: Australian Map Coloring
if __name__ == "__main__":
    # Variables (regions)
    variables = ['WA', 'NT', 'SA', 'QLD', 'NSW', 'VIC', 'TAS']

    # Domains (possible colors)
    domains = {v: ['Red', 'Green', 'Blue'] for v in variables}

    # Neighbors (adjacent regions)
    neighbors = {
        'WA': ['NT', 'SA'],
        'NT': ['WA', 'SA', 'QLD'],
        'SA': ['WA', 'NT', 'QLD', 'NSW', 'VIC'],
        'QLD': ['NT', 'SA', 'NSW'],
        'NSW': ['SA', 'QLD', 'VIC'],
        'VIC': ['SA', 'NSW'],
        'TAS': []
    }

    # Solve
    solver = MapColoringCSP(variables, domains, neighbors)
    solution = solver.backtracking_search()

    # Output
    if solution:
        print("Map Coloring Solution:")
        for region, color in solution.items():
            print(f"{region}: {color}")
    else:
        print("No valid coloring found.")
