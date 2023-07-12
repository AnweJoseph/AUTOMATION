from jinja2 import Environment, FileSystemLoader, StrictUndefined
import yaml

def saved_config():
    config = yaml.full_load(open('./data.yml'))
    
    env = Environment(loader = FileSystemLoader('.'), trim_blocks=True)
    template = env.get_template('ospf_template.j2')
    output = template.render(config)
    
    save_template = open('ospf_configs', 'w')
    save_template.write(output)
    save_template.close
