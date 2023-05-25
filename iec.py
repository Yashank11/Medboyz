from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('templates'))
t = env.get_template('foo.html')
print(t.render(name='Luther'))