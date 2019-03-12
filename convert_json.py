import json, io
import json as J
import glob, os

try:
    to_unicode = unicode
except NameError:
    to_unicode = str

###############################################################################
def convert_file_to_json(path_to_open, path_to_write):
    data = {}
    line_counter = 0

    raw_file = open(path_to_open, 'r')
    for line in raw_file.readlines():
        line = line.replace('\t', ',', 1)
        a_data = line.split(',')
        if line_counter == 0:   # Si esta es la primera linea del archivo
            key1 = a_data[0]
            key2 = a_data[1].strip()
            data[key1] = []
            data[key2] = []
        else:
            data[key1].append(a_data[0])
            data[key2].append(a_data[1].strip())
        line_counter = line_counter + 1
    split_path  = path_to_open.split('/')
    json_name = split_path[len(split_path) - 1]
    print('JSON_NAME = ' + json_name)
    file_name = path_to_write + '/' + json_name
    with io.open(file_name.replace('.dat','.json'), 'w', encoding='utf8') as outfile:
        str_ = json.dumps(data, indent = 2, sort_keys = True, separators = (',', ': '), ensure_ascii=False)
        outfile.write(to_unicode(str_))


def cvrt_fle_to_json(path_to_open):
    data = {}
    line_counter = 0

    raw_file = open(path_to_open, 'r')
    for line in raw_file.readlines():
        line = line.replace('\t', ',', 1)
        a_data = line.split(',')
        if line_counter == 0:   # Si esta es la primera linea del archivo
            key1 = a_data[0]
            key2 = a_data[1].strip()
            data[key1] = []
            data[key2] = []
        else:
            data[key1].append(a_data[0])
            data[key2].append(a_data[1].strip())
    
        line_counter = line_counter + 1
    return data
        
if __name__ == '__main__':
    convert_file_to_json('/home/delcracnk/REPOSITORIES/Bank_Models/01Sk_HSphere/Benny_Version/data/sk_HSpheere.dat', '/home/delcracnk/Web_Site/daniela/Esfera_Dura')
