def get_total(costs,items,tax):
    cost_without_tax = 0
    for item in items:
        if item in costs:
            cost_without_tax += costs[item]
    return "{:.2f}".format(cost_without_tax + (cost_without_tax * tax))

costs = {'socks':5, 'shoes':60, 'sweater':30}
result = get_total(costs, ['shirt', 'socks', 'shoes'], 0.09)
print(result)

