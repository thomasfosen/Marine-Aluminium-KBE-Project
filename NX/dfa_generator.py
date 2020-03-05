import re
class Generator():

    def __init__(self):
        self.dfa_template_location = ''
        self.dfa_target = 'node_template'

    def read_dfa_template(self, target):
        return open(target + '.dfa', "r").read()

    def get_dfa_parameters(self, target):
        dfa = self.read_dfa_template(target)

        #extracts parameter area: everything between template start and end
        #for some reason '.*?' didn't work..
        parameter_section = re.findall(r'#template_start[\D\d\t\n\s:]*#template_end', dfa)
        #print(parameter_section[0])

        vars = re.findall(r'\)\s*(.+?):', parameter_section[0]) #locate everything that is between < >
        vals = re.findall(r':\s*(\d+?);', parameter_section[0]) #locate default values

        return vars,vals

        #testing
        for var in vars:
            print(var)

    def generate_dfa(self, template, vars, customer_form):
        dfa = self.read_dfa_template(template)
        for var in vars:
            if var in customer_form:
                value = customer_form[var]
                dfa = re.sub('<(' + var + '.+?);',  var + ':' + value + ';', dfa)

        dfa = re.sub('My_Node',  'My_Node_Generated',    dfa)

        f = open(template + "_generated.dfa", "w")
        f.write(dfa)

    def change_node_diameter(self, diameter):
        template = 'node_template'
        dfa = self.read_dfa_template(template)
        dfa = re.sub('My_Node',  'My_Node_Generated',    dfa)
        dfa = re.sub('(' + 'sphere_diameter' + '.+?);',  'sphere_diameter' + ':' + str(diameter) + ';', dfa)

        f = open(template + "_generated.dfa", "w")
        f.write(dfa)

    def filter(self, val):
        return val.split('#', 1)[-1]


cake = Generator()
array = cake.get_dfa_parameters('node_template')
# print(array)

print(array[1])
array[1][0]=136
print(array)
# test['sphere_diameter'] = 123

# cake.generate_dfa('node_template', array[0], array)
cake.change_node_diameter(200)
