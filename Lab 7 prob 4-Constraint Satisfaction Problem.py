# Implement CSP to allocate resources such as computer servers or office space, taking into
# account the needs of different departments or projects, the availability of resources, and any
# budget constraints.


from constraint import Problem

def allocate_resources(resources, departments, budget_constraints):
    problem = Problem()

    # Define variables with domains (possible resources) for each department
    for department in departments:
        valid_resources = [res['name'] for res in resources if res['cost'] <= budget_constraints[department]]
        problem.addVariable(department, valid_resources)

    # Constraint to ensure each department gets a unique resource
    def unique_resources_constraint(*args):
        return len(args) == len(set(args))

    problem.addConstraint(unique_resources_constraint, departments)

    # Constraint to ensure that the selected resource is within the department's budget
    def budget_constraint(*args):
        for dept, resource in zip(departments, args):
            resource_cost = next(res['cost'] for res in resources if res['name'] == resource)
            if resource_cost > budget_constraints[dept]:
                return False
        return True

    problem.addConstraint(budget_constraint, departments)

    # Get solutions
    solutions = problem.getSolutions()
    return solutions

resources_list = [
    {'name': 'Server A', 'cost': 1000},
    {'name': 'Server B', 'cost': 1500},
    {'name': 'Office Space X', 'cost': 2000},
    {'name': 'Office Space Y', 'cost': 2500}
]

department_list = ['IT', 'HR', 'Finance', 'Marketing']
budget_limits = {'IT': 1500, 'HR': 2500, 'Finance': 1000, 'Marketing': 2000}

result_solutions = allocate_resources(resources_list, department_list, budget_limits)
for solution in result_solutions:
    print(solution)
