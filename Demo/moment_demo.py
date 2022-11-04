import moment

print(moment.now())

x = moment.now().strftime('%Y-%m-%d_%H-%M-%S-%f')
print(x)
